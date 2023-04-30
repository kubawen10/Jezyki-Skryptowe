import os
import sys
from SSHLogJournal import SSHLogJournal
from ipaddress import IPv4Address
from SSHFactory import SSHFactory
import SSHEntryClasses
from datetime import datetime

def readFile(path: str):
    if not os.path.isfile(path):
        print(f"Wrong path: {path}")
        sys.exit(1)
    
    with open(path) as file:
        for log in file:
            yield log

journal = SSHLogJournal()
for entry in readFile('./testLog.log'):
    journal.append(entry)

print("length: " + str(len(journal)))

last_entry_in_file = 'Dec 10 11:42:04 LabSZ sshd[28143]: Received disconnect from 183.62.140.253: 11: Bye Bye [preauth]'
obj = SSHEntryClasses.SSHOther(last_entry_in_file)

print("test __contains__: " + str(obj in journal))
print("slicing tests:")
print(journal[-1])
print(journal[-5::2])
print("\nget_ip_entries test: ")
print(journal.get_ip_entries(IPv4Address("183.62.140.253"))[-3:])
date=datetime.strptime('Dec 10 11:42:04', '%b %d %H:%M:%S')
print("dates:")
print(journal[date])


















