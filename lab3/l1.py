from l2 import *
from l3 import *


if __name__ == '__main__':
    log = read_log()
    test = get_entries_by_addr(log, "131.182.171.66")

    print("Num", len(test))

    print("##################################")
    print_entries(sort_log(test, 4))
    print("##################################")

    d = log_to_dict(test)
    print_dict_entry_dates(d)