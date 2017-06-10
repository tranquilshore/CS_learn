class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.data = key
        
def leafcount_iterative(root):
    if root is None:
        return 0
    
    s = []
    s.append(root)
    count = 0
    while s:
        current = s.pop()
        if current.left is None and current.right is None:
            count += 1
        if current.right:
            s.append(current.right)
        if current.left:
            s.append(current.left)
    return count

def leafcount_recursive(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1
    else:
        return leafcount_recursive(root.left) + leafcount_recursive(root.right)
    
        
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.right.left = Node(6)
root.left.right.right = Node(7)

print leafcount_recursive(root)