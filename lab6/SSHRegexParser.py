import re
from datetime import datetime
from typing import List

class SSHRegexParser:
    def get_primary_info_from_entry(entry: str):
        LOG_PATTERN = re.compile(r"(?P<date>\w+\s+\d+\s\d{2}:\d{2}:\d{2})\s(?P<host>.+)\ssshd\[(?P<pid>\d+)\]:\s(?P<message>.+)")
        pattern_match = LOG_PATTERN.match(entry)
        date = datetime.strptime(pattern_match.group('date'), '%b %d %H:%M:%S')
        host = pattern_match.group('host')
        pid = int(pattern_match.group('pid'))
        message = pattern_match.group('message')
        return date, host, pid, message
    
    def get_IPs_from_message(message: str) -> List[str]:
        IPV4_PATTERN = re.compile(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}")
        return IPV4_PATTERN.findall(message)
    
    def is_failed_password(entry: str):
        FAILED_PASSWORD_PATTERN = re.compile(r"Failed password for") 
        return FAILED_PASSWORD_PATTERN.search(entry)
    
    def is_accepted_password(entry: str):
        ACCEPTED_PASSWORD_PATTERN = re.compile(r"Accepted password for")
        return ACCEPTED_PASSWORD_PATTERN.search(entry)
    
    def is_error(entry: str):
        ERROR_PATTERN = re.compile(r"error:")
        return ERROR_PATTERN.search(entry)
    
    def get_failed_password_info_from_message(message: str):
        FAILED_PASSWORD_PATTERN = re.compile(r"Failed password for\s+(invalid user\s+)?(?P<user>.+) from \d+\.\d+\.\d+\.\d+ port (?P<port>\d+)") 
        return FAILED_PASSWORD_PATTERN.search(message).groupdict()
    
    def get_accepted_password_info_from_message(message: str):
        ACCEPTED_PASSWORD_PATTERN = re.compile(r"Accepted password for (?P<user>\w+) from \d+\.\d+\.\d+\.\d+ port (?P<port>\d+)")
        return ACCEPTED_PASSWORD_PATTERN.search(message).groupdict()
    
    def get_error_info_from_message(message: str):
        ERROR_PATTERN = re.compile(r"error: (?P<error_message>.+)")
        return ERROR_PATTERN.search(message).groupdict()
     