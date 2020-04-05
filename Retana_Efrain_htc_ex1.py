#Starter code by Olac Fuentes
"""
@Author: Efrain Retana
@Professor: Olac Fuentes
@Assignment: HashTable Chaining  
"""

import hash_table_chain as htc
import math

def load_factor(h):
    # sum the length of all the buckets in the hashtable
    sum = 0
    for list in h.bucket:
        sum += len(list)
    # return the average of the sum
    return sum/len(h.bucket)

def longest_bucket(h):
    # find the longest bucket in the hashtable and return the amonunt
    max = - math.inf
    #compare lengths until max is found
    for list in h.bucket:
        if len(list) > max:
            max = len(list)
    return max

def check(h):
    #iterate through amount of buckets
    for i in range(len(h.bucket)):
        # to check that it is in right place, take current list key and find mod 
        # by num of buckets and compare to i
        for list in h.bucket[i]:
            if list.key % len(h.bucket) != i:
                return False
    return True

def has_duplicates(L):
    #create new table size of list
    tempH = htc.HashTableChain(len(L))
    
    # for each num in the list insert into new hashtable and if it returns -1
    # then data is duplicate
    for num in L:
        if tempH.insert(num,num) == -1:
            return True
    return False

if __name__ == "__main__":
    h = htc.HashTableChain(9)
    
    players = ['Bellinger','Betts', 'Hernandez', 'Pederson', 'Pollock', 'Taylor']
    numbers= [35, 50, 14, 31, 11, 3]

    for i in range(len(players)):
        h.insert(numbers[i],players[i])
        
    h.print_table()

    print(load_factor(h))  # 0.66666666666666
    
    print(longest_bucket(h)) # 2
    
    print(check(h)) # True
    h.bucket[2][0].key = 2302
    h.print_table()
    print(check(h)) # False
    
    L1 = [1,4,2,5,6,7,8,39,20,45]
    L2 = [1,4,2,5,6,7,8,39,20,45,9,13,5,34]
    
    print(has_duplicates(L1)) # False
    print(has_duplicates(L2)) # True
