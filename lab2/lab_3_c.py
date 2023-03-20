import sys
import utils

def get_biggest_file():
    biggest = 0
    path = ''
    for line in sys.stdin:
        bytes_value = utils.get_number_of_bytes(line)
        if(bytes_value > biggest):
            try:
                path = utils.get_path(line)
                biggest = bytes_value
            except Exception:
                # if there is an error when getting path, pass this line
                pass

    print(path, biggest)

if __name__ == '__main__':
    get_biggest_file()


