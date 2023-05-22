from SSHRegexParser import SSHRegexParser
from SSHEntryClasses import *


class SSHFactory:
    @staticmethod
    def get_entry_class(entry: str) -> 'SSHFailedPassword' | 'SSHAcceptedPassword' | 'SSHError' | 'SSHOther':
        if SSHRegexParser.is_failed_password(entry):
            return SSHFailedPassword(entry)
        if SSHRegexParser.is_accepted_password(entry):
            return SSHAcceptedPassword(entry)
        if SSHRegexParser.is_error(entry):
            return SSHError(entry)     
        return SSHOther(entry)
    
