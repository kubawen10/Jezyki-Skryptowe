import sys
import utils

def read_log():
    list_of_tuples = []
    
    for line in sys.stdin:
        try:
            list_of_tuples.append(utils.make_tuple(line.rstrip()))
        except Exception:
            pass
    return list_of_tuples

def sort_log(log, sort_by):
    try:
        return sorted(log, key = lambda entry: entry[sort_by])
    except IndexError:
        print("Couldnt sort log! Index error!")
        return None
    
def get_entries_by_addr(log, addr):
    return [entry for entry in log if entry[0] == addr]

def get_entries_by_code(log, code):
    return [entry for entry in log if entry[3] == code and code in [200, 302, 404]]

def get_failed_reads(log, connect=False):
    if connect:
        return [entry for entry in log if utils.is4xx(entry[3]) or utils.is5xx(entry[3])]
    else: 
        return [entry for entry in log if utils.is4xx(entry[3])], [entry for entry in log if utils.is5xx(entry[3])]

def get_entries_by_extension(log, extension):
    return [entry for entry in log if entry[2].endswith(extension)]

def print_entries(log):
    for entry in log:
        print(entry)