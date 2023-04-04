import sys
import os
import subprocess
import utils

if __name__ == '__main__':
    if len(sys.argv) != 2 or not os.path.isdir(sys.argv[1]):
        print("Wrong arguments! You should provide path to directory you want to analyze")
        sys.exit(1)
    
    results = {"Num of files": 0,
               "Chars_sum": 0,
               "Words_sum": 0,
               "Lines_sum": 0,
               "Most often_char": '',
               "Most_often_word": ''}
    
    most_often_char = {}
    most_often_word = {}
    for filename in os.listdir(sys.argv[1]):
        path_to_file = os.path.join(sys.argv[1], filename)
        
        proc = subprocess.Popen(['python', 'text_file_analyzer.py', path_to_file], stdout = subprocess.PIPE)
        if proc.returncode != None:
            print(proc.stdout.readline().decode().rstrip())
            continue
        line = proc.stdout.readline().decode().rstrip().split(',')

        results["Num of files"] +=1
        results["Chars_sum"] += int(line[1])
        results["Words_sum"] += int(line[2])
        results["Lines_sum"] += int(line[3])
        
        char = line[4]
        word = line[5]
        utils.count_occurance(char, most_often_char)
        utils.count_occurance(word, most_often_word)   
    
    results["Most often_char"] = utils.get_most_occurant(most_often_char)
    results["Most_often_word"] = utils.get_most_occurant(most_often_word)
    
    for k,v in results.items():
        print(f'{k}: {v}', end='\t\t')
    print()