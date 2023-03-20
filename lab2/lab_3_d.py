import sys
import utils

def get_graphics_download_ratio():
    graphics_bytes = 0
    all_bytes = 0
    for line in sys.stdin:
        bytes_value = utils.get_number_of_bytes(line)
        try:
            if(bytes_value != 0 and utils.get_path(line).endswith(('.gif', '.jpg', '.jpeg', '.xbm'))):
                graphics_bytes += bytes_value
            all_bytes += bytes_value
        except Exception:
            # if there is an error when getting path, pass this line
            pass

    try:
        print(graphics_bytes/all_bytes)
    except ZeroDivisionError:
        print("Couldn't calculate ratio")

if __name__ == '__main__':
    get_graphics_download_ratio()