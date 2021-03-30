# -*- coding: utf-8 -*-



#Returnerer en boolean som angiver om nøglen k er i træet T (side 290-291)
def search(T, k):
    
    
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


