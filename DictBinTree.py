# -*- coding: utf-8 -*-



#Returnerer en boolean som angiver om nøglen k er i træet T (side 290-291)
# def search(T, k):

#virker ikke helt efter hensigten. 
A = [15,6,18,3,7,17,20,2,4,13,9]

#Returnerer index for den ønskede key
def TREE_SEARCH(x,k):
    if x == None or k == A[x]:
        return x
    if k < A[x]:
        return TREE_SEARCH(x*2+1,k)
    else:
        return TREE_SEARCH(x*2+2,k)
    
    

#print(TREE_SEARCH(0,7))
    
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
        T = z     # Tree was empty, create root 
    elif key(z) < key(y):
        y[1] = z
    else:
        y[2] = z
    

    

#Returnerer en liste med nøglerne i træet T i en sorteret orden (side 288) 
def orderedTraversal(T):
    tree_list = []
    traverse_recursive(root(T), tree_list)
    return tree_list
    
def traverse_recursive(x, tree_list):
    if x != None:
        traverse_recursive(left(x), tree_list)
        tree_list.append(key(x))
        traverse_recursive(right(x), tree_list)

#Returnerer et nyt og tomt træ
def createEmptyDict():
    return [[None]]



def key(x):
    return x[0]

def left(x):
    return x[1]

def right(x):
    return x[2]

def root(T):
    return T[0]



T = [[5,[2,None,None], [6, None, None]]]
z = [3, None, None]
z2 = [7, None, None]

insert(T, z)

print(T)

print(orderedTraversal(T))





