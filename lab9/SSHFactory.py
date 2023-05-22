from SSHRegexParser import SSHRegexParser
from SSHEntryClasses import *
from typing import Union


class SSHFactory:
    @staticmethod
    def get_entry_class(entry: str) -> Union['SSHFailedPassword', 'SSHAcceptedPassword', 'SSHError', 'SSHOther']:
        if SSHRegexParser.is_failed_password(entry):
            return SSHFailedPassword(entry)
        if SSHRegexParser.is_accepted_password(entry):
            return SSHAcceptedPassword(entry)
        if SSHRegexParser.is_error(entry):
            return SSHError(entry)     
        return SSHOther(entry)
    
