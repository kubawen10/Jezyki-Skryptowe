from ipaddress import IPv4Address
import re
from datetime import datetime

class SSHLogEntry:
    LOG_PATTERN = re.compile(r"(?P<date>\w+\s+\d+\s\d{2}:\d{2}:\d{2})\s(?P<host>.+)\ssshd\[(?P<pid>\d+)\]:\s(?P<message>.+)")
    IPV4_PATTERN = re.compile(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}")
    
    def __init__(self, entry: str) -> None:
        pattern_match = SSHLogEntry.LOG_PATTERN.match(entry)
        self.date = datetime.strptime(pattern_match.group('date'), '%b %d %H:%M:%S')
        self.host = pattern_match.group('host')
        self.pid = int(pattern_match.group('pid')),
        self.message = pattern_match.group('message')
    
    def __str__(self) -> str:
        date_str = self.date.strftime('%b %d, %H:')
    
    def get_ip(self) -> IPv4Address|None:
        ips = SSHLogEntry.IPV4_PATTERN.findall(self.message)
        
        if len(ips) > 0:
            return ips[0]
        else:
            return None
    
    
    