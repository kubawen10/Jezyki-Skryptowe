import os

def specify_backup_directory():
    # if BACKUP_DIR provided use it as backup directory
    if 'BACKUPS_DIR' in os.environ:
        return os.environ['BACKUPS_DIR']
    else: 
        return os.path.join(os.path.expanduser('~'), '.backups')
    
def count_occurance(x, dictionary):
    if x in dictionary:
        dictionary[x] += 1
    else:
        dictionary[x] = 1
        
def get_most_occurant(dictionary):
    sorted_dict = sorted(dictionary.items(), key=lambda x:x[1], reverse=True)
    if len(sorted_dict) != 0:
        return sorted_dict[0][0]
    else:
        return ''