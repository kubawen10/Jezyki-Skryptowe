import os
from parser_z2 import *
def readFile(path: str):
    if not os.path.isfile(path):
        print(path)
        print("Wrong path")
        return []
    
    with open(path) as file:
        for log in file:
            yield parse_entry(log)

if __name__ == '__main__':
    for a in readFile('./shorter.log'):
        print(get_message_type(a.message))
