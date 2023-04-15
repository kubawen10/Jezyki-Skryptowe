import os
from parser_z2 import *
from logging_z3 import *
from statistics_z4 import *

def readFile(path: str):
    if not os.path.isfile(path):
        print(path)
        print("Wrong path")
        return []
    
    with open(path) as file:
        for log in file:
            yield log

if __name__ == '__main__':
    logger = get_loggin_function()
    entries = []
    user_entries_acc = get_user_entries_accumulation_function()

    for log in readFile('./SSH.log'):
        parsed_entry = parse_entry(log)
        entries.append(parsed_entry)

        #logger(parsed_entry)

        #user_entries_acc(parsed_entry)

    
    #print(get_n_random_entries_from_random_user(user_acc(None)))
    #print(get_least_and_most_logged_in_users(user_entries_acc(None)))
    #print(get_session_time_mean_and_stddev(entries))
    print(get_user_session_time_mean_and_stddev(entries))





# opens with Accepted password or 


        
