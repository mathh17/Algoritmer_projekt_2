# -*- coding: utf-8 -*-



#Returnerer en boolean som angiver om nøglen k er i træet T (side 290-291)
def search(T, k):
    pass
    
    
#Indsæt nøglen k i træet T (side 294)
def insert(T, z):
    y = None
    x = root(T)
    while x != None:
        y = x
        if key(z) < key(x):
            x = left(x)
        else:
            x = right(x)        
    if y == None:
        T[0] = z     # Tree was empty, create root 
    else if key(z) < key(y):
        y[1] = z
    else:
        y[2] = z
    

    

#Returnerer en liste med nøglerne i træet T i en sorteret orden (side 288) 
def orderedTraversal(T):
    tree_list = []
    traverse_recursive(T.root)
    return tree_list
    
def traverse_recursive(x):
    if x != None:
        traverse_recursive(left(x))
        tree_list.append(x)
        traverse_recursive(right(x))

#Returnerer et nyt og tomt træ
def createEmptyDict():
    return [None]



def key(x):
    return x[0]

def left(x):
    return x[1]

def right(x):
    return x[2]

def root(x):
    return x[0]

