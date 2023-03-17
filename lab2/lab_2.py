import sys

# prints every line of given file
if __name__ == '__main__':
    for line in sys.stdin:
        print(line.rstrip())
