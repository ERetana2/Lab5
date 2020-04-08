
"""
@Author: Efrain Retana
@Professor: Olac Fuentes
@Assignment: Lab 5
"""

import numpy as np
import os
import hash_table_chain as htc
import math
        
def get_word_list(text):
    # Receives a string containing a document
    # Returns a list of strings containing the words in the document
    text = text.lower()
    word_list = []
    curr_wrd = ''
    for c in text:
        if ord(c)>=97 and ord(c)<=122:
            curr_wrd = curr_wrd+c
        else:
            if len(curr_wrd)>0:
                word_list.append(curr_wrd)
                curr_wrd = ''
    return word_list

def load_factor(h):
    # sum the length of all the buckets in the hashtable
    sum = 0
    for list in h.bucket:
        sum += len(list)
    # return the average of the sum
    return sum/len(h.bucket)

def long_buckets(h):
    # find buckets >= 1 and return the number
    sum = 0
    
    for bucket in h.bucket:
        if len(bucket) >= 2:
            sum += len(bucket)
    return sum

def longest_bucket(h):
    # find longest bucket and return length
    max = -math.inf
    
    for i in range(len(h.bucket)):
        if len(h.bucket[i]) >= max:
            max = len(h.bucket[i])
    return max

def create_htc(FileName): # generate a hashtable containing the stop words of text document 
# passes the name of the file containing the stop words
# returns a hashtable containing all the stop words
    f = open(FileName)
    text = f.read()
    f.close()
    wl = get_word_list(text)
    
    h = htc.HashTableChain(len(wl))
    for word in wl:
        h.insert(word,word)
        
    return h

def remove_stopWords(h_stopWords,wl):
    count = i = 0
    length = len(wl)
    for index in range(len(wl)):
        if h_stopWords.retrieve(wl[index]) != None:
            wl.remove(wl[index])
            count += 1
            
    return count
    

def empty_buckets(h):
    count = 0
    for bucket in h.bucket:
        if len(bucket) <= 0:
            count += 1
    return count

def numKeys(h): # return num of keys in hashtable
    numKeys = 0
    for bucket in h.bucket:
        numKeys += len(bucket)
    return numKeys
        
    
if __name__ == '__main__':
    h_stopWords = create_htc('stop_words.txt')

    #-----------STATS--------------#
    print('---------------------------------')
    print('Analysis of Stop Word hash table:')
    print('Total Buckets:',len(h_stopWords.bucket),', total Records:',numKeys(h_stopWords),
          ', load Factor: {0:.3f}'.format(load_factor(h_stopWords)))
    print('Empty Bucket Fraction in Table: {0:.2f}'.format(empty_buckets(h_stopWords)/len(h_stopWords.bucket)))
    print('Long bucket fraction in table: {0:.3f}'.format(long_buckets(h_stopWords)/len(h_stopWords.bucket)))
    print('Length longest Bucket in Table -> Length:',longest_bucket(h_stopWords))
    print('---------------------------------')
    
    abs_dir = '.\\abstracts\\'  # abstracts folder must be in current folder
    abstracts =   sorted(os.listdir(abs_dir)) # Abstract contains a lsit with all abstract file names

    for abstract in abstracts:
        h_abs = create_htc(abs_dir+abstract)
        f = open(abs_dir+abstract, 'r', encoding="utf8")
        text = f.read()
        f.close()
        wl = get_word_list(text)
        print('\n---------------------------------')
        print('File:',abstract)
        
        print('Total words:',len(wl),',total non-stop words:',len(wl)-remove_stopWords(h_stopWords,wl))
        print('Analysis of',abstract,'hash table')
        print('Total Buckets:',len(h_abs.bucket),', total Records:',numKeys(h_abs),
              ', load Factor: {0:.3f}'.format(load_factor(h_abs)))
        print('Empty Bucket Fraction in Table: {0:.2f}'.format(empty_buckets(h_abs)/len(h_abs.bucket)))
        print('Long bucket fraction in table: {0:.3f}'.format(long_buckets(h_abs)/len(h_abs.bucket)))
        print('Length longest Bucket in Table -> Length:',longest_bucket(h_abs))
        
        print('Word list')
        # break # Uncomment to run a single iteration

