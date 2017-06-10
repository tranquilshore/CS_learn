class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.data = key
def spiralorder_iterative(root):
    if root is None:
        return
    s1 = []
    s2 = []
    s1.append(root)
    
    while s1 or s2:
        while s1:
            current = s1.pop()
            print current.data,
            if current.right:
                s1.append(current.right)
            if current.left:
                s1.append(current.left)
        
        while s2:
            current = s2.pop()
            print current.data,
            if current.left:
                s2.append(current.left)
            if current.right:
                s2.append(current.right)
        
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print spiralorder_iterative(root)
