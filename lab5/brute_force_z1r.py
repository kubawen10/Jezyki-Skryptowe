from typing import List, Dict
from parser_z2 import *

def get_failed_entries_from_ips(entries: List[log_entry]) -> Dict[str, log_entry]:
    ip_failed_entries = dict()

    for entry in entries:
        if get_message_type(entry.message) == MessageType.FAILED_PASSWORD:
            ip = get_ipv4s_from_entry(entry)[0]

            if ip in ip_failed_entries:
                ip_failed_entries[ip].append(entry)
            else:
                ip_failed_entries[ip] = [entry]

    return ip_failed_entries

def get_ip_user_failed_entries_dict(ip_failed_entries: Dict[str, List[log_entry]]) -> Dict[str, Dict[str, log_entry]]:
    ip_user_entries = dict()

    for ip, entries in ip_failed_entries.items():
        user_entries = dict()
        for entry in entries:
            user = get_user_from_entry(entry)
            if user in user_entries:
                user_entries[user].append(entry)
            else:
                user_entries[user] = [entry]
        ip_user_entries[ip] = user_entries 
    return ip_user_entries      

def is_bruteforce(entries: List[log_entry], interval):
    entries_len = len(entries)
    for i in range(len(entries)):
        if i == entries_len-1:
            return False
        
        if abs((entries[i].date - entries[i+1].date).total_seconds()) <= interval:
            return True
        
    return False



def detect_bruteforce(entries: List[log_entry], max_interval, single_user=False):
    ip_failed_entries = get_failed_entries_from_ips(entries)

    if single_user:
        ip_user_failed_entries = get_ip_user_failed_entries_dict(ip_failed_entries)

        ip_user_bruteforces = []

        for ip, user_failed_entries in ip_user_failed_entries.items():
            for user, failed_entries in user_failed_entries.items():
                if is_bruteforce(failed_entries, max_interval):
                    ip_user_bruteforces.append((ip, user))

        return ip_user_bruteforces
    else:
        ip_bruteforces = []
        for ip, failed_entries in ip_failed_entries.items():
            if is_bruteforce(failed_entries, max_interval):
                ip_bruteforces.append(ip)

        return ip_bruteforces







