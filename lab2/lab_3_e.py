import sys
import utils

def get_code_200_requests():
    for line in sys.stdin:
        if(utils.get_request_code(line) == 200):
            print(line.rstrip())

if __name__ == '__main__':
    get_code_200_requests()