import sys
import utils 

def get_requests_between_22_and_6():
    for line in sys.stdin:
        try:
            utils.get_path(line)
            hour = utils.get_hour(line)
            if hour < 6 or hour > 22:
               #print(line.rstrip())
               pass
        except (TypeError, Exception):
            # if there is an error when getting hour, pass this line
            pass

if __name__ == '__main__':
    get_requests_between_22_and_6()
