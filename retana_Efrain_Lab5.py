
"""
@author: Efrain Retana
@Professor: Olac Fuentes
@Assignment: Lab 5
"""
import read_text_files as rtc
import os
import hash_table_chain as htc
import Retana_Efrain_htc_ex1 as

def h_stop_words():
    f = open('stop_words.txt', 'r', encoding="utf8")
    text = f.read()
    f.close()
    stopWords = rtc.get_word_list(text)
    
    h = htc.HashTableChain(len(stopWords))
    for word in stopWords:
        h.insert(word,word)
        
    return h

if __name__ == '__main__':
    abs_dir = '.\\abstracts\\'  # abstracts folder must be in current folder
    abstracts =   sorted(os.listdir(abs_dir)) # Abstract contains a lsit with all abstract file names
    
    print('The list of files to analyze is:')
    print(abstracts)
    
    h = h_stop_words()
    h.print_table()
    
    
    # for abstract in abstracts:
    #     f = open(abs_dir+abstract, 'r', encoding="utf8")
    #     print('\nFile:',abstract)
    #     text = f.read()
    #     f.close()
    #     print('Original text')
    #     print(text)
    #     wl = rtc.get_word_list(text)
    #     print('Word list')
    #     print(wl)
    #     break # Uncomment to run a single iteration