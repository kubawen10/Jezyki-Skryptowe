import logging
import sys
from parser_z2 import log_entry, MessageType, get_message_type


def logging_config(logging_level=logging.DEBUG):
    logging_formater = logging.Formatter("%(asctime)s\t%(levelname)s: %(message)s")

    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.DEBUG)
    console_handler.setFormatter(logging_formater)
    console_handler.addFilter(lambda x: x.levelno<=logging.WARNING)

    error_handler = logging.StreamHandler(sys.stderr)
    error_handler.setLevel(logging.ERROR)
    error_handler.setFormatter(logging_formater)

    logger = logging.getLogger()
    logger.setLevel(logging_level)
    logger.addHandler(console_handler)
    logger.addHandler(error_handler)

#calculates bytes of an entry that has been parsed, must add some consts
def bytes_of_entry(entry: log_entry):
    # 3 letters + _ + 2 digits or _digit + _ + 2digits + : + 2digits + : + 2digits + _
    bytes_for_date = 16
    bytes_for_host = len(entry.host)
    #len('sshd')
    bytes_for_app_and_braces = 4
    #len('[]: ')
    bytes_for_skipped_chars = 4
    bytes_for_message = len(entry.message)

    return bytes_for_date + bytes_for_host + bytes_for_app_and_braces + bytes_for_skipped_chars + bytes_for_message

def get_loggin_function(logging_level=logging.DEBUG):
    logging_config(logging_level)
    
    def logging_function(entry: log_entry):
        logging.debug(f"Bytes read: {bytes_of_entry(entry)}")

        msg_type = get_message_type(entry.message)
        msg_name = msg_type.name


        if msg_type in (MessageType.SUCCESSFUL_LOGIN, MessageType.SESSION_CLOSED):
            logging.info(msg_name)
        elif msg_type == MessageType.UNSUCCESSFUL_LOGIN:
            logging.warning(msg_name)
        elif msg_type in (MessageType.FAILED_PASSWORD, MessageType.INVALID_USERNAME):
            logging.error(msg_name)
        elif msg_type == MessageType.BREAK_IN:
            logging.critical(msg_name)
        
    return logging_function
