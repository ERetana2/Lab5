import matplotlib.pyplot as plt
import numpy as np
import bst

def bst_3nodes(L): # builds a tree with 3 Nodes
    T=bst.BST()
    T.insert(L[1])
    T.insert(L[0])
    T.insert(L[2])
    return T

def has_depth(T,d): # checks if the tree has depth d
    if type(T) == bst.BST:
        T = T.root
    depth = False
    if T is None:
        return depth
    if d == 0:
        if T != None:
            depth = True
            return depth
    return has_depth(T.left,d-1) or has_depth(T.right,d-1)
    
def add_n(T,n): # adds n to each element in every node
    if type(T) == bst.BST:
        T = T.root
    if T is None:
        return
    T.data += n
    add_n(T.left,n)
    add_n(T.right,n)
        
def get_path(T,k): #iterative approach to problem
    if type(T) == bst.BST:
        T = T.root
    temp = T
    path , found= '', False
    while temp is not None:
        if temp.data == k:
            found = True
            break
        if k < temp.data:
            path += 'L'
            temp = temp.left
        else:
            path += 'R'
            temp = temp.right
    if not found:
        return None
    return path
        
    # path = ''
    # found = False
    # if T is None:
    #     return ''
    # if k == T.data:
    #     found = True
    # if k < T.data:
    #     cur ='L'
    #     path = cur + get_path(T.left,k)
    # else:
    #     cur ='R'
    #     path = cur + get_path(T.right,k)
    
    # return path

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
    add_n(T,5)   
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
    
    
    
    
    
    
    
    
    
    
    
    