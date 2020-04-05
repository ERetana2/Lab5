
"""
@author: Efrain Retana
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

def long_bucket(h):
    # find buckets >= 1 and return the number
    sum = 0
    
    for list in h.bucket:
        if len(list) >= 1:
            sum += 1
    return sum

def h_stop_words(): # generate a hashtable containing the stop words of text document 
# passes the name of the file containing the stop words
# returns a hashtable containing all the stop words
    f = open('stop_words.txt')
    text = f.read()
    f.close()
    stopWords = get_word_list(text)
    print(len(stopWords))
    
    h = htc.HashTableChain(len(stopWords))
    for word in stopWords:
        sum = ''
        for char in word:
            sum += str(ord(char))
        h.insert(int(sum),word)
        
    return h

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
    h = h_stop_words()
    # h.print_table()
    print()
    #-----------STATS--------------#
    numKeys = numKeys(h)
    print('Analysis of Stop Word Table:\n---------------------------------')
    print('Total Buckets:',len(h.bucket),', Total Records:',numKeys,', Load Factor: {0:.3f}'.format(load_factor(h)))
    print('Empty Bucket Fraction in Table: {0:.3f}'.format(empty_buckets(h)/len(h.bucket)))
    print('Long Bucket Fraction in Table: {0:.3f}'.format(long_bucket(h)/len(h.bucket)))
    
    
    
    # abs_dir = '.\\abstracts\\'  # abstracts folder must be in current folder
    # abstracts =   sorted(os.listdir(abs_dir)) # Abstract contains a lsit with all abstract file names
    
    # print('The list of files to analyze is:')
    # print(abstracts)
    
    # for abstract in abstracts:
    #     f = open(abs_dir+abstract, 'r', encoding="utf8")
    #     print('\nFile:',abstract)
    #     text = f.read()
    #     f.close()
    #     print('Original text')
    #     print(text)
    #     wl = get_word_list(text)
    #     print('Word list')
    #     print(wl)
    #     break # Uncomment to run a single iteration

