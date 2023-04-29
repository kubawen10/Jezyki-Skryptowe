from ipaddress import IPv4Address
from SSHRegexParser import SSHRegexParser
import abc

class SSHLogEntry(metaclass = abc.ABCMeta):
    def __init__(self, entry: str) -> None:
        self.date, self.host, self.pid, self.message = SSHRegexParser.get_primary_info_from_entry(entry)
        self._raw_message = entry
        
    def __str__(self) -> str:
        date_str = self.date.strftime('%d %B %H:%M')
        return f"Date: {date_str}\t\tHost: {self.host}\tPid: {self.pid}\tMessage: {self.message}"
    
    def get_ip(self) -> IPv4Address|None:
        ips = SSHRegexParser.get_IPs_from_message(self.message)
        
        if len(ips) > 0:
            return IPv4Address(ips[0])
        else:
            return None
        
    @abc.abstractmethod
    def validate(self):
        date, host, pid, message = SSHRegexParser.get_primary_info_from_entry(self._raw_message)
        if not (self.date == date and self.host == host and self.pid == pid and self.message == message):
            return False
        return True
    
    @property
    def has_ip(self):
        return self.get_ip() != None
    
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}: {self.__dict__}"
    
    def __eq__(self, other) -> bool:
        return not (self > other or self < other)
    
    def __gt__(self, other):
        return (self.date, self.host, self.pid, self.message) > (other.date, other.host, other.pid, other.message)
    
    def __lt__(self, other):
        return (self.date, self.host, self.pid, self.message) < (other.date, other.host, other.pid, other.message)
    

class SSHFailedPassword(SSHLogEntry):
    def __init__(self, entry: str) -> None:
        super().__init__(entry)
        info = SSHRegexParser.get_failed_password_info_from_message(self.message)
        self.user = info['user']
        self.port = info['port']
        
    def validate(self):
        if not super().validate():
            return False
        
        info = SSHRegexParser.get_failed_password_info_from_message(self.message)
        return self.user == info['user'] and self.port == info['port']
    

class SSHAcceptedPassword(SSHLogEntry):
    def __init__(self, entry: str) -> None:
        super().__init__(entry)
        info = SSHRegexParser.get_accepted_password_info_from_message(self.message)
        self.user = info['user']
        self.port = info['port']
        
    def validate(self):
        if not super().validate():
            return False
        
        info = SSHRegexParser.get_accepted_password_info_from_message(self.message)
        return self.user == info['user'] and self.port == info['port']
    

class SSHError(SSHLogEntry):
    def __init__(self, entry: str) -> None:
        super().__init__(entry)
        info = SSHRegexParser.get_error_info_from_message(self.message)
        self.error_message = info['error_message']
    
    def validate(self):
        if not super().validate():
            return False
        
        info = SSHRegexParser.get_error_info_from_message(self.message)
        return self.error_message == info['error_message']
    

class SSHOther(SSHLogEntry):
    def __init__(self, entry: str) -> None:
        super().__init__(entry)
        
    def validate(self):
        return True
        