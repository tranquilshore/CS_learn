class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.data = key
        self.nextRight = None

        
def getnextRight(q):
    temp = q.nextRight
    
    while not temp is None:
        if temp.left:
            return temp.left
        if temp.right:
            return temp.right
        temp = temp.nextRight
    return None
        
def connect(root):
    if root is None:
        return
    root.nextRight = None
    
    while not root is None:
        q = root
        while not q is None:
            if q.left:
                if q.right:
                    q.left.nextRight = q.right
                else:
                    q.left.nextRight = getnextRight(q)
            if q.right:
                q.right.nextRight = getnextRight(q)
            q = q.nextRight
        
        if root.left:
            root = root.left
        elif root.right:
            root = root.right
        else:
            root = getnextRight(root)
        

        
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
