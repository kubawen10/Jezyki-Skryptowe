from l2 import *
from l3 import *

if __name__ == '__main__':
    log = read_log()
    from_addr = get_entries_by_addr(log, "129.94.144.152")
    
    #print_entries(from_addr)
    
    code_302 = get_entries_by_code(log, 302)
    #print_entries(code_302)
    
    sorted_by_bytes = sort_log(log, 4)
    #print_entries(sorted_by_bytes)
    #print_entries(sort_log(from_addr))
    
    failed = get_failed_reads(log, True)
    #print_entries(failed)
    
    jpg = get_entries_by_extension(log, ".jpg")
    print_entries(jpg)
    
    dict_of_jpg = log_to_dict(jpg)
    jpg_addr = get_addrs(dict_of_jpg)
    #print_dict_entry_dates(dict_of_jpg)
    
    
    
    