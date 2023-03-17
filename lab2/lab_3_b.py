import sys
import utils

def get_sum_of_data_sent_in_GB():
    sum_of_bytes = 0
    for line in sys.stdin:
        sum_of_bytes += utils.get_number_of_bytes(line)

    print(sum_of_bytes / (1024**3))

if __name__ == '__main__':
    get_sum_of_data_sent_in_GB()



