import argparse
import parser_z2
import statistics_z4

def configure_parser():
    parser = argparse.ArgumentParser(description="LOG file parser.", add_help=True)
    
    parser.add_argument("--path", help = "Path to .log file.", required=True)
    parser.add_argument("--level", choices=['d', 'i', 'w', 'e', 'c'], required=False, default="d", 
                        help="Minimal logging level, choices: d-DEBUG(default), i-INFO, w-WARNING, e-ERROR, c-CRITICAL")
    
    subparsers = parser.add_subparsers(title="subcomands", help="subcommand help", dest="subcommand")
    
    subparsers.add_parser("verbose", help="Verbose mode, prints every parsed line to stdout. (z2a)")
    subparsers.add_parser("ip", help="Print ip from entry messages if it is present. (z2b)")
    subparsers.add_parser("user", help="Print user from entry messages if it is present. (z2c)")
    subparsers.add_parser("type", help="Print type of entry messages. (z2d)")
    
    subparsers.add_parser("random_entries", help="Get random number of entries from random user. (z4a)")
    connection_subparser = subparsers.add_parser("connection_times", help="Get mean and stddev of connection times for whole file. -u or --user_connections for mean and stddev for each user (z4b)", add_help=True)
    connection_subparser.add_argument("-u", "--user_connections", action="store_true", help="Get mean and stddev of connection time for each user. (z4b2)")
    subparsers.add_parser("least_and_most", help="Get least and most ogged in users. (z4c)")
    print(parser.parse_args())
    return parser.parse_args()
    

def get_function_to_execute(args: argparse.Namespace):
    if args.subcommand == 'verbose':
        return parser_z2.parse_entry
    if args.subcommand == 'ip':
        return parser_z2.get_ipv4s_from_entry
    if args.subcommand == 'user':
        return parser_z2.get_user_from_entry
    if args.subcommand == 'type':
        return parser_z2.get_message_type  
    if args.subcommand == 'random_entries':
        return statistics_z4.get_n_random_entries_from_random_user
    if args.subcommand == 'connection_times':
        if args.user_connections:
            return statistics_z4.get_user_session_time_mean_and_stddev
        else:
            return statistics_z4.get_session_time_mean_and_stddev
    if args.subcommand == 'least_and_most':
        return statistics_z4.get_least_and_most_logged_in_users
    
if __name__ == '__main__':
    configure_parser()