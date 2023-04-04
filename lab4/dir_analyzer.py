import sys
import os
import subprocess

if __name__ == '__main__':
    if len(sys.argv) != 2 or not os.path.isdir(sys.argv[1]):
        print("Wrong arguments! You should provide path to directory you want to analyze")
        sys.exit(1)
        
    for filename in os.listdir(sys.argv[1]):
        path_to_file = os.path.join(sys.argv[1], filename)
        
        proc = subprocess.Popen(['python', 'text_file_analyzer.py', path_to_file], stdout = subprocess.PIPE)
        
        line = proc.