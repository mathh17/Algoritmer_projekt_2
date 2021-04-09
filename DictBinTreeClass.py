# -*- coding: utf-8 -*-

class dictBinTreeClass:
    
    #Returnerer en boolean som angiver om nøglen k er i træet T (side 290-291)
    def __init__(self):
        self.T = [None]
        
    
    def root(self, T):
        return self.T[0]
    
    def key(self, x):
        return x[0]
    
    def left(self, x):
        return x[1]
    
    def right(self, x):
        return x[2]
    
    def print_tree(self):
        print(self.T)




T = [[5,[2,None,None], [6, None, None]]]

T = dictBinTreeClass()
T.print_tree