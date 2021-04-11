"""
@author: Mathias Østergaard Hansen - mathh17
         Joachim Skovbogaard - Josko20
         Andreas Klauber - ankla20
"""

import sys
import DictBinTree as DB
#tomt nyt træ
T = DB.createEmptyDict()

#funktion der beder om input til træet
def treesort(T):
    for line in sys.stdin:
        DB.insert(T,int(line))
    

treesort(T)
#Ordered traversal funktion der returnerer en sorteret liste 
order = DB.orderedTraversal(T)
#Loop der udskriver listen fra ordered traversal én af gangen
for i in order:
        print(i)