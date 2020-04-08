
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
    # find buckets >= 2 and return the number
    sum = 0
    # 
    for bucket in h.bucket:
        if len(bucket) >= 2: # count number of buckets that are considered 'long'
            sum += 1
    return sum

def longest_bucket(h):
    # find longest bucket and return length
    max = -math.inf
    
    for i in range(len(h.bucket)):
        if len(h.bucket[i]) >= max: # compare longest lengths
            max = len(h.bucket[i])
    return max

def create_htc(wl): # generate a hashtable containing the stop words of text document 
    h = htc.HashTableChain(len(wl))
    for word in wl:
        h.insert(word,word) # insert key and value as the current word
        
    return h

def remove_stopWords(h_stopWords,wl):
    count = i = 0
    while i != len(wl): # update condition as len of wl changes
        if h_stopWords.retrieve(wl[i]) != None:
            wl.pop(i) # remove word from list
            i-= 1# readjust index to fit current element w/o skipping elements
            count += 1
        else:
            i += 1
    return count

def common_word(wl): # find the most common word in a list and return a tuple with most
    # amount of repetition as (word,amount of times)
    h = htc.HashTableChain(len(wl))
    max = '',0
    for word in wl:# iterate list and keep value as amount of times word has repeated
        if h.insert(word,1) == -1:
            newVal = h.retrieve(word) + 1 # update value if word repeates
            h.update(word,newVal)
            if newVal > max[1]: # if current value is greater than previous max, save current word
                max = word,newVal
        else:
            h.insert(word,1)
    return max

def empty_buckets(h):
    #iterate through table and count number of empty buckets
    count = 0
    for bucket in h.bucket:
        if len(bucket) <= 0:
            count += 1
    return count # return count of empty buckets

def numKeys(h): # return num of keys in hashtable
    numKeys = 0
    for bucket in h.bucket: # iterate through hashtable
        numKeys += len(bucket)
    return numKeys
        
    
if __name__ == '__main__':
    # read folder that contains all the abstracts
    abs_dir = '.\\abstracts\\'  # abstracts folder must be in current folder
    abstracts =   sorted(os.listdir(abs_dir)) # Abstract contains a lsit with all abstract file names
    f = open('stop_words.txt', 'r', encoding="utf8")
    text = f.read()
    f.close()
    wl = get_word_list(text)
    
    h_stopWords = create_htc(wl) # create a hashtable that contains stop words list

    #-----------STATS--------------#
    print('---------------------------------')
    print('Analysis of Stop Word hash table:')
    print('Total Buckets:',len(h_stopWords.bucket),', total Records:',numKeys(h_stopWords),
          ', load Factor: {0:.3f}'.format(load_factor(h_stopWords)))
    print('Empty Bucket Fraction in Table: {0:.2f}'.format(empty_buckets(h_stopWords)/len(h_stopWords.bucket)))
    print('Long bucket fraction in table: {0:.3f}'.format(long_buckets(h_stopWords)/len(h_stopWords.bucket)))
    print('Length longest Bucket in Table -> Length:',longest_bucket(h_stopWords))
    print('---------------------------------')

    for abstract in abstracts: # iterate through all the set of files in abstract folder and perform 
        # analysis
        f = open(abs_dir+abstract, 'r', encoding="utf8")
        text = f.read()
        f.close()
        wl = get_word_list(text)
        print('\n---------------------------------')
        print('File:',abstract)
        # print analysis of abstract
        print('Total words:',len(wl),',total non-stop words:',len(wl)-remove_stopWords(h_stopWords,wl))
        print('Analysis of',abstract,'hash table')
        h_abs = create_htc(wl) # create hashtable containing new list of words after removing stop words
        print('Total Buckets:',len(h_abs.bucket),', total Records:',numKeys(h_abs),
              ', load Factor: {0:.3f}'.format(load_factor(h_abs)))
        print('Empty Bucket Fraction in Table: {0:.3f}'.format(empty_buckets(h_abs)/len(h_abs.bucket)))
        print('Long bucket fraction in table: {0:.3f}'.format(long_buckets(h_abs)/len(h_abs.bucket)))
        print('Length longest Bucket in Table -> Length:',longest_bucket(h_abs))
        cWord = common_word(wl)
        print('Most common word:',cWord[0],'- occurs',cWord[1],'times')
        
        # break # Uncomment to run a single iteration

