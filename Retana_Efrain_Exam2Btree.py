"""
@Author: Efrain Retana
@Professor: Olac Fuentes
@TA: Oscar Galindo
"""

import matplotlib.pyplot as plt
import numpy as np
import btree

def find_k(T,k): # fix errors of the find_K implementation
    if type(T) == btree.BTree:
        T = T.root
    if k in T.data:
        return True
    if T.is_leaf:
        return False
    ch = 0
    for i in range(len(T.data)):
        if k < T.data[i]:
            ch = i
            return find_k(T.child[ch],k)
    return find_k(T.child[-1],k)

def roots_children(T): # returns a list containing the parent of the leaf nodes
    if type(T) == btree.BTree:
        T = T.root
    L = []
    for i in range(len(T.child)):
        if T.child[i].is_leaf:
            for num in T.data:
                if num not in L:
                    L.append(num)
        L += roots_children(T.child[i])
    return L

def prune_leaves(T): # remove all the leaves of btree
    if type(T) == btree.BTree:
        T = T.root
    for child in T.child:
        if child.is_leaf:
            T.child = []
            T.is_leaf = True
        prune_leaves(child)
    return

def make_binary(T): # makes a binary tree containing only the smallest elements of the btree
    if type(T) == btree.BTree:
        T = T.root
    if T.is_leaf:
        T.data = [T.data[0]]
        return
    T.child = [T.child[0],T.child[1]]
    T.data = [T.data[0]]
    for child in T.child:
        make_binary(child)
    return

if __name__ == "__main__":  
    plt.close('all') 
    T = btree.BTree()  
    T_empty = btree.BTree()  
    nums = [6, 3, 16, 11, 7, 17, 14, 8, 5, 19, 15, 1, 2, 4, 18, 13, 9, 20, 10, 12, 21]
    for num in nums:
        T.insert(num)
    T.draw('Original tree')  
    
    print('Question 1')
    print(find_k(T,10))    # True
    print(find_k(T,14))    # True
    print(find_k(T,9))     # True
    print(find_k(T,25))    # False
    
    print('Question 2')
    print(roots_children(T))        # [3, 7, 14, 17]
    print(roots_children(T_empty))  # []

    print('Question 3')
    T = btree.BTree()  
    for num in nums:
        T.insert(num)    
    prune_leaves(T)
    T.draw('Question 3') 
    
    print('Question 4')
    T = btree.BTree()  
    for num in nums:
        T.insert(num)    
    make_binary(T)
    T.draw('Question 4') 
    