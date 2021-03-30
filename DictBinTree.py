# -*- coding: utf-8 -*-



#Returnerer en boolean som angiver om nøglen k er i træet T (side 290-291)
def search(T, k):

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
    
    

print(TREE_SEARCH(0,7))
    
#Indsæt nøglen k i træet T (side 294)
def insert(T, k):
    

#Returnerer en liste med nøglerne i træet T i en sorteret orden (side 288) 
def orderedTraversal(T):
    tree_list = []
    traverse_recursive(T.root)
    
def traverse_recursive(x):
    if x != None:
        traverse_recursive(left(x))
        
        traverse_recursive(right(x))

#Returnerer et nyt og tomt træ
def createEmptyDict():
    return [None]


