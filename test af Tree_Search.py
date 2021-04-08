# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 11:17:58 2021

@author: Andreas
"""







#Returnerer index for den ønskede key
def TREE_SEARCH(k,T):
    print(T)      
    if k == T[0]:
        return True
    if k < T[0]:
        #tjekker on node i højre side er et blad
        if T[1] == None:
            return False
        #forsætter søgning til venstre side i træet
        return TREE_SEARCH(k,T[1])
    else:
        #tjekker on node i venstre side er et blad        
        if T[2] == None:
            return False        
        #forsætter søgning til højre side i træet
        return TREE_SEARCH(k,T[2])
    


k = 8
T = [5,[2,None,None],[8,None,[11,None,None]]]

    
    

print(TREE_SEARCH(k,T))