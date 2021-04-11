# -*- coding: utf-8 -*-

#Returnerer en boolean som angiver om nøglen k er i træet T (side 290-291)
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
    
#Indsæt nøglen k i træet T (side 294)
def insert(T, z):
    y = None
    x = root(T)
    while x != None:
        y = x
        if z < key(x):
            x = left(x)
        else:
            x = right(x)
            
    if y == None:
        T[0] = [z, None, None]     # Tree was empty, create root 
    elif z < key(y):
        y[1] = [z, None, None]
    else:
        y[2] = [z, None, None]
    

    

#Returnerer en liste med nøglerne i træet T i en sorteret orden (side 288) 
def orderedTraversal(T):
    tree_list = []
    traverse_recursive(root(T), tree_list)
    for i in tree_list:
        print(i)
    
def traverse_recursive(x, tree_list):
    if x != None:
        traverse_recursive(left(x), tree_list)
        tree_list.append(key(x))
        traverse_recursive(right(x), tree_list)

#Returnerer et nyt og tomt træ
def createEmptyDict():
    return [None]



def key(x):
    return x[0]

def left(x):
    return x[1]

def right(x):
    return x[2]

def root(T):
    return T[0]
