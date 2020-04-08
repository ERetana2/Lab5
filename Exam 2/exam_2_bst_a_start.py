import matplotlib.pyplot as plt
import numpy as np
import bst

def bst_3nodes(L):
    T=bst.BST()
    for i in range(3):
        T.insert(L[i])
    return T

def has_depth(T,d):
    if type(T) == bst.BST:
        T = T.root
    if d == 0:
        if T != None:
            has_depth = True
def add_n(T,n):
    return 
        
def get_path(T,k):
    return ''

if __name__ == "__main__":
    plt.close('all')
    
    print('Question 1')   
    L = [10,20,30]
    T=bst_3nodes(L)
    T.draw()
    
    A =[11, 6, 7, 16, 17, 2, 4, 18, 14, 8, 15, 1,  20, 13]
    T = bst.BST()
    for a in A:
        T.insert(a)
    T.draw()
    
    print('Question 2')     
    print(has_depth(T,0))                    # True
    print(has_depth(T,1))                    # True
    print(has_depth(T,2))                    # True
    print(has_depth(T,3))                    # True
    print(has_depth(T,4))                    # True
    print(has_depth(T,5))                    # False    
    print(has_depth(T,6))                    # False        
    
    print('Question 3')     
    print(add_n(T,5))   
    T.draw()
    
    A =[11, 6, 7, 16, 17, 2, 4, 18, 14, 8, 15, 1,  20, 13]
    T = bst.BST()
    for a in A:
        T.insert(a)
    T.draw()

    print('Question 4')     
    print(get_path(T,15))  # RLR
    print(get_path(T,1))   # LLL
    print(get_path(T,10))  # None
    
    
    
    
    
    
    
    
    
    
    
    