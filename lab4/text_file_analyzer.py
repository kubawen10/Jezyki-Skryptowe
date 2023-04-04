import sys
import os

if __name__ == '__main__':
    if len(sys.argv) != 2 or not os.path.isfile(sys.argv[1]):
        print("Wrong arguments! You should provide path to file you want to analyze")
        sys.exit(1)
        
    path_to_file = os.path.abspath(sys.argv[1])
    char_num = 0
    word_num = 0
    most_often_char = {}
    most_often_word = {}
        
    with open(path_to_file, 'r') as file:
        lines = file.readlines()
        lines_num = len(lines)
        
        for line in lines:
            splited = line.rstrip().split()
            word_num += len(splited)
            
            for word in splited:
                char_num += len(word)
                
                if word in most_often_word:
                    most_often_word[word] += 1
                else:
                    most_often_word[word] = 1
                    
                for char in word:
                    if char in most_often_char:
                        most_often_char[char] += 1
                    else:
                        most_often_char[char] = 1
                        
    sorted_words = sorted(most_often_word.items(), key=lambda x:x[1], reverse=True)
    if len(sorted_words) != 0:
        most_often_word=sorted_words[0][0]
    else:
        most_often_word=''
    
    sorted_chars = sorted(most_often_char.items(), key=lambda x:x[1], reverse=True)
    if len(sorted_chars) != 0:
        most_often_char = sorted_chars[0][0]
    else:
        most_often_char=''
        
    print(path_to_file, char_num, word_num, lines_num, most_often_char, most_often_word, sep=',')  
            
            
            

        
        
        
        
    