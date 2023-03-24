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


def sort_log(log, sortBy):
    try:
        return sorted(log, key = lambda entry: entry[sortBy])
    except IndexError:
        print("Couldnt sort log! Index Error")
        return None
    
def get_entries_by_addr(log, addr):
    return [entry for entry in log if entry[0] == addr] 
    # return [entry for entry in log if entry[0]==addr and entry[3] == 200] 

def get_entries_by_code(log, code):
    return [entry for entry in log if entry[3] == code]

def get_failed_reads(log, connect=False):
    if connect:
        return [entry for entry in log if utils.is4xx(entry[3]) or utils.is5xx(entry[3])]
    else: 
        return [entry for entry in log if utils.is4xx(entry[3])], [entry for entry in log if utils.is5xx(entry[3])]
    
def get_entries_by_extension(log, extension):
    return [entry for entry in log if entry[2].endswith(extension)]

def print_entries(entries):
    for entry in entries:
        print(entry)
