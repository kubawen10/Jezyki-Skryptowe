import sys
import os
import csv
import shutil
from subprocess import run

import utils

def remove_contents(target):
    for filename in os.listdir(target):
        file_path = os.path.join(target, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))

def choose_archive(data):
    data.reverse()
    for i, row in enumerate(data):
        print(f'{i}: {row}')

    choice = int(input("Choose archive to restore: "))

        
    while choice < 0 or len(data)-1 < choice:
        choice = int(input("Wrong input, choose correct number: "))

    return data[choice]

if __name__ == '__main__':
    # if no arg, use curdir as dest
    if len(sys.argv) == 1:
        dest = os.path.curdir
    # if one argument provided, use it as dest
    elif len(sys.argv) == 2:
        dest = sys.argv[1]   
    # if more than one argument provided exit program
    else:
        print("Incorrect arguments! You should provide zero or one argument that specifies directory")
        sys.exit()

    # specify the backup directory from which we want to unzip
    source_dir = utils.specify_backup_directory()

    if not os.path.isfile(os.path.join(source_dir, 'history.csv')):
        print("No archive to restore in backup folder!")
        sys.exit()

    with open(os.path.join(source_dir, 'history.csv'), 'r') as history:
        data = list(csv.DictReader(history))

    archive_to_restore = choose_archive(data)['copied_to']
    archive_to_restore = os.path.join(source_dir, archive_to_restore)

    # if dest isnt empty remove its content
    if os.path.isdir(dest):
            remove_contents(dest)

    run(['unzip', archive_to_restore, '-d', dest])
    