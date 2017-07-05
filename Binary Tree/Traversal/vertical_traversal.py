#dictionary initialisation requirements
from collections import defaultdict
dctnry = defaultdict(list)
#dctnry = defaultdict(lambda:0)

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.data = key
        
def vertical_order(root):
    if root is None:
        return
    
    hd = 0
    
    q = []
    q.append((root,hd))
    
    while len(q) > 0:
        tmp = q[0]
        q.pop(0)
        
        hd = tmp[1]
        node = tmp[0]
        
        dctnry[hd].append(node.data)
        
        if node.left is not None:
            q.append((node.left, hd-1))
        if node.right is not None:
            q.append((node.right, hd+1))
    
    for k in dctnry.items():
        print k[1]
        print "\n"
        
        
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.right.left = Node(6)
root.left.right.right = Node(7)

vertical_order(root)
