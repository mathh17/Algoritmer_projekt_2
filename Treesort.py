import sys
import DictBinTree as DB

T = DB.createEmptyDict()

def treesort(T):
    for line in sys.stdin:
        DB.insert(T,int(line))
    DB.orderedTraversal(T)

treesort(T)

print("Please enter the key you want to search for:")
for line in sys.stdin:
    print(DB.search(T,int(line)))