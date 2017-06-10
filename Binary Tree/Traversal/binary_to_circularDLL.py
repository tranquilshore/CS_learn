class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.data = key
        
def concatenate(leftlist, rightlist):
    if leftlist is None:
        return rightlist
    if rightlist is None:
        return leftlist
    
    #last nodes of two DLLs
    leftlast = leftlist.left
    rightlast = rightlist.left
    
    #updating connections
    leftlast.right = rightlist
    rightlast.left = leftlast
    
    leftlist.left = rightlast
    rightlast.right = leftlist
    
    return leftlist

#function to convert a tree to circular linked list

def btreetoclist(root):
    if root is None:
        return
    #recursively convert left and right subtrees
    left = btreetoclist(root.left)
    right = btreetoclist(root.right)
    
    #circular linked list of a single node
    root.left = root.right = root
    
    return concatenate(concatenate(left,root), right)

def printclist(head):
    tmp = head
    while True:
        print tmp.data,
        tmp = tmp.right
        if tmp == head:
            break
root = Node(10)
root.left = Node(12)
root.right = Node(15)
root.left.left = Node(25)
root.left.right = Node(30)
root.right.left = Node(36)

head = btreetoclist(root)
printclist(head)