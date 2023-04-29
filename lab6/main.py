import os
import sys
from SSHLogJournal import SSHLogJournal
from ipaddress import IPv4Address

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




