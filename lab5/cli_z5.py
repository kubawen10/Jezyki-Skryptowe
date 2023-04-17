import argparse

def configure_parser():
    parser = argparse.ArgumentParser(description="LOG file parser.", add_help=True)
    
    parser.add_argument("path", help = "Path to .log file.", required=True)
    parser.add_argument("-l", "--level", choices=['d', 'i', 'w', 'e', 'c'], required=False, default="d", 
                        help="Minimal logging level, choices: d-DEBUG(default), i-INFO, w-WARNING, e-ERROR, c-CRITICAL")
    parser.add_argument("-v", "--verbose", action="store_true", help="Verbose mode, prints every parsed line to stdout. (z2a)")
    parser.add_argument("i", "--ip", action="store_true", help="Prints ip from entry messages if it is present. (z2b)")
    parser.add_argument("u", "--user", action="store_true", help="Prints user from entry messages if it is present. (z2c)")
    