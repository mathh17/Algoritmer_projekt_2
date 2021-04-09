# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 11:17:58 2021

@author: Andreas
"""



def search(T,k):
    x = root(T)
    return tree_search(x,k)

#Returnerer index for den ønskede key
def tree_search(T, k):     
    if k == key(T):
        return True
    if k < key(T):
        #tjekker on node i højre side er et blad
        if left(T) == None:
            return False
        #forsætter søgning til højre side i træet
        return tree_search(left(T), k)
    else:
        #tjekker on node i venstre side er et blad        
        if right(T) == None:
            return False        
        #forsætter søgning til venstre side i træet
        return tree_search(right(T), k)


def key(x):
    return x[0]

def left(x):
    return x[1]

def right(x):
    return x[2]

def root(T):
    return T[0]



k = 3
T = [[5,[2,None,None],[8,None,[11,None,None]]]]

    
    

print(search(T, k))



