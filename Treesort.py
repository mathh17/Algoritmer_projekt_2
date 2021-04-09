import sys
import DictBinTree as DB

T = DB.createEmptyDict()

def treesort(T):
    for line in sys.stdin:
        DB.insert(T,int(line))
    print(DB.orderedTraversal(T))

treesort(T)

print(T)


for line in sys.stdin:
    print("Please enter the key you want to search for:")
    print(DB.search(T,line))