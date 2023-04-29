import abc
from SSHRegexParser import SSHRegexParser
import SSHEntryClasses

class SSHFactory(metaclass = abc.ABCMeta):
    @abc.abstractmethod
    def create_ssh_object(entry: str) -> SSHEntryClasses.SSHLogEntry:
        pass

    def get_entry_class(entry: str):
        if SSHRegexParser.is_failed_password(entry):
            return SSHFailedFactory.create_ssh_object(entry)
        if SSHRegexParser.is_accepted_password(entry):
            return SSHAcceptedFactory.create_ssh_object(entry)
        if SSHRegexParser.is_error(entry):
            return SSHErrorFactory.create_ssh_object(entry)     
        return SSHOtherFactory.create_ssh_object(entry)
    

class SSHFailedFactory(SSHFactory):
    def create_ssh_object(entry: str):
        return SSHEntryClasses.SSHFailedPassword(entry)
    

class SSHAcceptedFactory(SSHFactory):
    def create_ssh_object(entry: str):
        return SSHEntryClasses.SSHAcceptedPassword(entry)
    

class SSHErrorFactory(SSHFactory):
    def create_ssh_object(entry: str):
        return SSHEntryClasses.SSHError(entry)
    

class SSHOtherFactory(SSHFactory):
    def create_ssh_object(entry: str):
        return SSHEntryClasses.SSHOther(entry)
