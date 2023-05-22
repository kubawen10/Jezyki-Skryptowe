from ipaddress import IPv4Address
from SSHRegexParser import SSHRegexParser
import abc
from datetime import datetime
from typing import List, Dict

class SSHLogEntry(metaclass = abc.ABCMeta):
    def __init__(self, entry: str) -> None:
        self.date: datetime
        self.host: str
        self.pid: int
        self.message: str
        self.date, self.host, self.pid, self.message = SSHRegexParser.get_primary_info_from_entry(entry)
        self._raw_message: str = entry
        
    def __str__(self) -> str:
        date_str: str = self.date.strftime('%d %B %H:%M')
        return f"Date: {date_str}\t\tHost: {self.host}\tPid: {self.pid}\tMessage: {self.message}"
    
    def get_ip(self) -> IPv4Address|None:
        ips: List[str] = SSHRegexParser.get_IPs_from_message(self.message)
        
        if len(ips) > 0:
            return IPv4Address(ips[0])
        else:
            return None
        
    @abc.abstractmethod
    def validate(self) -> bool:
        date: datetime
        host: str
        pid: int
        message: str
        date, host, pid, message = SSHRegexParser.get_primary_info_from_entry(self._raw_message)
        if not (self.date == date and self.host == host and self.pid == pid and self.message == message):
            return False
        return True
    
    @property
    def has_ip(self) -> bool:
        return self.get_ip() != None
    
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}: {self.__dict__}"
    
    def __eq__(self, other) -> bool:
        return not (self > other or self < other)
    
    def __gt__(self, other) -> bool:
        return (self.date, self.pid, self.message) > (other.date, other.pid, other.message)
    
    def __lt__(self, other) -> bool:
        return (self.date, self.pid, self.message) < (other.date, other.pid, other.message)
    

class SSHFailedPassword(SSHLogEntry):
    def __init__(self, entry: str) -> None:
        super().__init__(entry)
        info: Dict[str, str] = SSHRegexParser.get_failed_password_info_from_message(self.message)
        self.user: str = info['user']
        self.port: str = info['port']
        
    def validate(self) -> bool:
        if not super().validate():
            return False
        
        info: Dict[str, str] = SSHRegexParser.get_failed_password_info_from_message(self.message)
        return self.user == info['user'] and self.port == info['port']
    

class SSHAcceptedPassword(SSHLogEntry):
    def __init__(self, entry: str) -> None:
        super().__init__(entry)
        info: Dict[str, str] = SSHRegexParser.get_accepted_password_info_from_message(self.message)
        self.user: str = info['user']
        self.port: str = info['port']
        
    def validate(self) -> bool:
        if not super().validate():
            return False
        
        info: Dict[str, str] = SSHRegexParser.get_accepted_password_info_from_message(self.message)
        return self.user == info['user'] and self.port == info['port']
    

class SSHError(SSHLogEntry):
    def __init__(self, entry: str) -> None:
        super().__init__(entry)
        info: Dict[str, str] = SSHRegexParser.get_error_info_from_message(self.message)
        self.error_message: str = info['error_message']
    
    def validate(self) -> bool:
        if not super().validate():
            return False
        
        info: Dict[str, str] = SSHRegexParser.get_error_info_from_message(self.message)
        return self.error_message == info['error_message']
    

class SSHOther(SSHLogEntry):
    def __init__(self, entry: str) -> None:
        super().__init__(entry)
        
    def validate(self) -> bool:
        return True
        