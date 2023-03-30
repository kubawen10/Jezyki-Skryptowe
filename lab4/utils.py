import os

def specify_backup_directory():
    # if BACKUP_DIR provided use it as backup directory
    if 'BACKUPS_DIR' in os.environ:
        return os.environ['BACKUPS_DIR']
    else: 
        return os.path.join(os.path.expanduser('~'), '.backups')