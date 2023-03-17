import sys

def get_requests_from_poland():
    for line in sys.stdin:
        try:
            address = line.split()[0]
            if(address.endswith('.pl')):
                print(line.rstrip())
        except IndexError:
            # if there is an error when getting path, pass this line
            pass


if __name__ == '__main__':
    get_requests_from_poland()