from datetime import datetime

def make_tuple(line):
    return get_address(line), get_date(line), get_path(line), get_code(line), get_bytes(line)

def get_address(line):
    return line.split()[0]

def get_date(line):
    date_str = line.split()[3].lstrip('[')
    return datetime.strptime(date_str, '%d/%b/%Y:%H:%M:%S')

def get_path(line):
    path = line.split('"')[1].split()
    return path[1]

def get_code(line):
    return int(line.split()[-2])

def get_bytes(line):
    bytes_value = line.split()[-1]
    return 0 if bytes_value == '-' else int(bytes_value)

def is4xx(code):
    return code >= 400 and code < 500

def is5xx(code):
    return code >=500 and code < 600