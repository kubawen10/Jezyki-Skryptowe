import re
from datetime import datetime
from typing import List, Tuple, Dict

# this class contains static methods used for parsing information from entries using regex
class SSHRegexParser:
    @staticmethod
    def get_primary_info_from_entry(entry: str) -> Tuple[datetime, str, int, str]:
        LOG_PATTERN: re.Pattern[str] = re.compile(r"(?P<date>\w+\s+\d+\s\d{2}:\d{2}:\d{2})\s(?P<host>.+)\ssshd\[(?P<pid>\d+)\]:\s(?P<message>.+)")
        pattern_match: re.Match[str] | None = LOG_PATTERN.match(entry)
        assert pattern_match is not None
        date: datetime = datetime.strptime(pattern_match.group('date'), '%b %d %H:%M:%S')
        host: str = pattern_match.group('host')
        pid: int = int(pattern_match.group('pid'))
        message: str = pattern_match.group('message')
        return date, host, pid, message
    
    @staticmethod
    def get_IPs_from_message(message: str) -> List[str]:
        IPV4_PATTERN: re.Pattern[str] = re.compile(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}")
        return IPV4_PATTERN.findall(message)
    
    @staticmethod
    def is_failed_password(entry: str) -> re.Match[str] | None:
        FAILED_PASSWORD_PATTERN: re.Pattern[str] = re.compile(r"Failed password for") 
        return FAILED_PASSWORD_PATTERN.search(entry)
    
    @staticmethod
    def is_accepted_password(entry: str) -> re.Match[str] | None:
        ACCEPTED_PASSWORD_PATTERN: re.Pattern[str] = re.compile(r"Accepted password for")
        return ACCEPTED_PASSWORD_PATTERN.search(entry)
    
    @staticmethod
    def is_error(entry: str) -> re.Match[str] | None:
        ERROR_PATTERN: re.Pattern[str] = re.compile(r"error:")
        return ERROR_PATTERN.search(entry)
    
    @staticmethod
    def get_failed_password_info_from_message(message: str) -> Dict[str, str]:
        FAILED_PASSWORD_PATTERN: re.Pattern[str] = re.compile(r"Failed password for\s+(invalid user\s+)?(?P<user>.+) from \d+\.\d+\.\d+\.\d+ port (?P<port>\d+)") 
        pattern_match: re.Match[str] | None = FAILED_PASSWORD_PATTERN.search(message)
        assert pattern_match is not None
        groupdict: Dict[str, str] = pattern_match.groupdict()
        return groupdict
    
    @staticmethod
    def get_accepted_password_info_from_message(message: str) -> Dict[str, str]:
        ACCEPTED_PASSWORD_PATTERN: re.Pattern[str] = re.compile(r"Accepted password for (?P<user>\w+) from \d+\.\d+\.\d+\.\d+ port (?P<port>\d+)")
        pattern_match: re.Match[str] | None = ACCEPTED_PASSWORD_PATTERN.search(message)
        assert pattern_match is not None
        groupdict: Dict[str, str] = pattern_match.groupdict()
        return groupdict
    
    @staticmethod
    def get_error_info_from_message(message: str) -> Dict[str, str]:
        ERROR_PATTERN: re.Pattern[str] = re.compile(r"error: (?P<error_message>.+)")
        pattern_match: re.Match[str] | None = ERROR_PATTERN.search(message)
        assert pattern_match is not None
        groupdict: Dict[str, str] = pattern_match.groupdict()
        return groupdict
     