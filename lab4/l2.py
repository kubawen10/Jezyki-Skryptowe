import sys
import os
from pathlib import Path


if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.argv[1] == '-d':
        for dir in os.environ['PATH'].split(os.pathsep):
            print(dir)
    elif len(sys.argv) == 2 and sys.argv[1] == '-f':
        for dir in os.environ['PATH'].split(os.pathsep):
            list_of_files = [f for f in os.listdir(dir) if os.path.isfile(os.path.join(dir, f))]
            print(f"Directory: {dir}\nFiles: {list_of_files}", end='\n\n')
    else:
        print("Incorrect arguments!\nYou can run this script with 'directories' or 'files' parameter")
