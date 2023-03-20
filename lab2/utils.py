import sys
from datetime import datetime

def is_valid(line):
    return len(line.split()) == 10

def get_request_code(line):
    try:
        code = int(line.split()[-2])
        return code
    except (IndexError, ValueError):
        return None
    
def get_path(line):
    path = line.split('"')[1].split()
    if len(path) == 3 or len(path) == 2: 
        return path[1]
    else:
        print(line)
        raise Exception("Wrong format!")

def get_number_of_given_code_requests(code):
    num = 0
    for line in sys.stdin:
        if(code == get_request_code(line)):
            num += 1
    return num

def get_number_of_bytes(line):
    try:
        bytes_value = line.split()[-1]
    except IndexError:
        return 0
    
    if(bytes_value == '-'):
        return 0
    else:
        try:
            return int(bytes_value)
        except ValueError:
            return 0

# this function is much faster than using get_date().hour
def get_hour(line):
    try:
        date_str = line.split()[3]
        return int(date_str.split(':')[1])
    except IndexError:
        return None


def get_date(line):
    try: 
        date_str = line.split()[3].lstrip('[')
        return datetime.strptime(date_str, '%d/%b/%Y:%H:%M:%S')
    except (IndexError, ValueError):
        return None