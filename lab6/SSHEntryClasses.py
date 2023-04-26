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
        self.pid = int(pattern_match.group('pid'))
        self.message = pattern_match.group('message')
    
    def __str__(self) -> str:
        date_str = self.date.strftime('%d %B %H:%M')
        return f"Date: {date_str}\t\tHost: {self.host}\tPid: {self.pid}\tMessage: {self.message}"
    
    def get_ip(self) -> IPv4Address|None:
        ips = SSHLogEntry.IPV4_PATTERN.findall(self.message)
        
        if len(ips) > 0:
            return ips[0]
        else:
            return None
        
        
test = SSHLogEntry("Dec 10 07:07:38 LabSZ sshd[24206]: pam_unix(sshd:auth): check pass; user unknown")
print(test)

class SSHFailedPassword(SSHLogEntry):
    FAILED_PASSWORD_PATTERN = re.compile(r"^Failed password for (invalid user )?(?P<user>\w+) from \d+\.\d+\.\d+\.\d+ port (?P<port>\d+) (?P<protocol>.+)")
    pass

class SSHAcceptedPassword(SSHLogEntry):
    ACCEPTED_PASSWORD_PATTERN = re.compile(r"^Accepted password for (?P<user>\w+) from \d+\.\d+\.\d+\.\d+ port (?P<port>\d+) (?P<protocol>.+)")
    pass

class SSHError(SSHLogEntry):
    ERROR_PATTERN = re.compile(r"error: (?P<error_message>.+)")
    pass

class SSHOther(SSHLogEntry):
    pass
    
    
    