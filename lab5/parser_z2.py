import re
from collections import namedtuple
from datetime import datetime
from enum import Enum

LOG_PATTERN = re.compile(r"(?P<date>\w+\s+\d+\s\d{2}:\d{2}:\d{2})\s(?P<host>.+)\ssshd\[(?P<pid>\d+)\]:\s(?P<message>.+)")
log_entry = namedtuple("Log_Entry", ['date', 'host', 'pid', 'message'])

def parse_entry(entry: str):
    match = LOG_PATTERN.match(entry)
    if not match:
        print(entry)
    return log_entry(datetime.strptime(match.group('date'), '%b %d %H:%M:%S'),
                     match.group('host'),
                     int(match.group('pid')),
                     match.group('message'))


IPV4_PATTERN = re.compile(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}")

def get_ipv4s_from_entry(entry: log_entry):
    return IPV4_PATTERN.findall(entry.message)

# accepts: user=name ; user name; but not: user request or user authentication
USER_PATTERN = re.compile(r"(?<=[^r]user[=\s])(?!request)(?!authentication)(\w+)")

def get_user_from_entry(entry: log_entry):
    match = USER_PATTERN.search(entry.message)
    return match.group(0) if match else None

SUCCESSFUL_LOGIN_PATTERN = re.compile(r'Accepted password for')
SESSION_CLOSED_PATTERN = re.compile(r'session closed|Received disconnect|Connection closed|Disconnecting:|Connection reset')
#UNSUCCESSFUL_LOGIN_PATTERN = re.compile(r'authentication failure')
UNSUCCESSFUL_LOGIN_PATTERN = re.compile(r'^(?!PAM).+(authentication failure)')
FAILED_PASSWORD_PATTERN = re.compile(r'Failed password for')
INVALID_USERNAME_PATTERN = re.compile(r'[I,i]nvalid user')
BREAK_IN_PATTERN = re.compile(r"POSSIBLE BREAK-IN ATTEMPT")

message_pattern_list = [
    SUCCESSFUL_LOGIN_PATTERN,
    SESSION_CLOSED_PATTERN,
    UNSUCCESSFUL_LOGIN_PATTERN,
    FAILED_PASSWORD_PATTERN,
    INVALID_USERNAME_PATTERN,
    BREAK_IN_PATTERN
]

class MessageType(Enum):
    SUCCESSFUL_LOGIN = 0
    SESSION_CLOSED = 1
    UNSUCCESSFUL_LOGIN = 2
    FAILED_PASSWORD = 3
    INVALID_USERNAME = 4
    BREAK_IN = 5
    OTHER = 6

def get_message_type(message: str):
    for i, pattern in enumerate(message_pattern_list):
        if pattern.search(message):
            return MessageType(i)
    return MessageType["OTHER"]