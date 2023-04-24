import argparse

def configure_parser():
    parser = argparse.ArgumentParser(description="LOG file parser.", add_help=True)
    
    parser.add_argument("--path", help = "Path to .log file.", required=True)
    parser.add_argument("--level", choices=['d', 'i', 'w', 'e', 'c'], required=False, default="d", 
                        help="Minimal logging level, choices: d-DEBUG(default), i-INFO, w-WARNING, e-ERROR, c-CRITICAL")
    
    subparsers = parser.add_subparsers(title="subcomands", help="Subcommand help", dest="subcommand")
    
    subparsers.add_parser("verbose", help="Verbose mode, prints every parsed line. (z2a)")
    subparsers.add_parser("ip", help="Print ip from entry messages if it is present. (z2b)")
    subparsers.add_parser("user", help="Print user from entry messages if it is present. (z2c)")
    subparsers.add_parser("type", help="Print type of entry messages. (z2d)")
    
    subparsers.add_parser("random_entries", help="Get random number of entries from random user. (z4a)")
    connection_subparser = subparsers.add_parser("connection_times", help="Get mean and stddev of connection times for whole file. -u or --user_connections for mean and stddev for each user (z4b)", add_help=True)
    connection_subparser.add_argument("-u", "--user_connections", action="store_true", help="Get mean and stddev of connection time for each user. (z4b2)")
    subparsers.add_parser("least_and_most", help="Get least and most logged in users. (z4c)")
    bruteforce_subparser = subparsers.add_parser("bruteforce", help="Detect bruteforce attempts. (z1r)")
    bruteforce_subparser.add_argument("-i", "--interval", type=int, help="Maximum interval between attempts. Default = 5", default=5)
    bruteforce_subparser.add_argument("-u", "--user", action="store_true", help="Detect attacks on single username.")

    return parser