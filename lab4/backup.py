import sys
import os
from datetime import datetime
from subprocess import run
import csv
import utils
if __name__ == '__main__':
    # validate args
    if len(sys.argv) != 2 or not os.path.isdir(sys.argv[1]):
        print("Incorrect argument! You should provide directory you want to backup.")
        sys.exit()

    # check if backup directory was specified, if not use default
    target_dir = utils.specify_backup_directory()

    if not os.path.exists(target_dir):
        os.mkdir(target_dir)

    # create filename
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    dirname = os.path.basename(os.path.abspath(sys.argv[1]))
    filename = f"{timestamp}-{dirname}.zip"

    target_file = os.path.join(target_dir, filename)
    run(['zip', '-r', target_file, sys.argv[1]])

    file_exists = os.path.isfile(os.path.join(target_dir, 'history.csv'))

    # add csv file
    with open(os.path.join(target_dir, 'history.csv'), 'a') as history:
        field_names = ['datetime', 'copied_from', 'copied_to']
        
        row = {
            'datetime': timestamp,
            'copied_from': os.path.abspath(sys.argv[1]),
            'copied_to': filename
        }
        
        dictwriter = csv.DictWriter(history, fieldnames=field_names)
        if not file_exists:
            dictwriter.writeheader()
            
        dictwriter.writerow(row)
