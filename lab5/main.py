import os
import sys
from parser_z2 import *
from logging_z3 import *
from statistics_z4 import *
from cli_z5 import *
from brute_force_z1r import detect_bruteforce

def readFile(path: str):
    if not os.path.isfile(path):
        print(f"Wrong path: {path}")
        sys.exit(1)
    
    with open(path) as file:
        for log in file:
            yield log

if __name__ == '__main__':
    args = configure_parser().parse_args()
    path=args.path
    logging_level=args.level
    subcommand=args.subcommand

    logger = get_logging_function(logging_level)
    entries = []

    for log in readFile(path):
        parsed_entry = parse_entry(log)
        entries.append(parsed_entry)

        #logger(parsed_entry)

        if subcommand == 'verbose':
            print(parsed_entry)
        elif subcommand == 'ip':
            print('IPs: ', get_ipv4s_from_entry(parsed_entry))
        elif subcommand == 'user':
            print('User: ', get_user_from_entry(parsed_entry))
        elif subcommand == 'type':
            print('Message type: ', get_message_type(parsed_entry.message).name)  
        
    if subcommand == 'random_entries':
        user, entries = get_n_random_entries_from_random_user(entries)
        print(f'Random {len(entries)} entries from {user}: {entries}')
    elif subcommand == 'connection_times':
        if args.user_connections:
            for user, (mean, stddev) in get_user_session_time_mean_and_stddev(entries).items():
                print(f"User's {user}\tMean connection time: {mean:.3f}\tStddev: {stddev:.3f}")
        else:
            mean, stddev = get_session_time_mean_and_stddev(entries)
            print(f"Mean connection time: {mean:.3f}\tStddev: {stddev:.3f}")
    elif subcommand == 'least_and_most':
        least, most = get_least_and_most_logged_in_users(entries)
        print(f"Least logged user: {least}\t Most logged user: {most}")
    elif subcommand == 'bruteforce':
        if args.user:
            print("Detected bruteforce attacks for (ip, user): ", detect_bruteforce(entries, args.interval, True))
        else:
            print("Detected bruteforce attacks for ips: ", detect_bruteforce(entries, args.interval, False))
