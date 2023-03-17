import sys
import utils

def get_requests_on_friday():
    for line in sys.stdin:
        try:
            if utils.get_date(line).weekday() == 4:
                print(line.rstrip())
        except TypeError:
            # if there is an error when getting path, pass this line
            pass

if __name__ == '__main__':
    get_requests_on_friday()
