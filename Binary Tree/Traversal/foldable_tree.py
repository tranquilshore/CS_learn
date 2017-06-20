class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.data = key
        
def mirror_i(root):
    if root is None:
        return
    s = []
    s.append(root)
    while s:
        current = s.pop()
        
        temp = current.right
        current.right = current.left
        current.left = temp
        
        if current.right:
            s.append(current.right)
        if current.left:
            s.append(current.left)

def isfoldable(root):
    if root is None:
        return True
    mirror_i(root.left)
    res = is_struc_same(root.left, root.right)
    mirror_i(root.right)
    return res

def is_struc_same(a, b):
    if a is None and b is None:
        return True
    if a is not None and b is not None and is_struc_same(a.left, b.left) and is_struc_same(a.right, b.right):
        return True
    return False
    
        
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.right = Node(4)
root.right.left = Node(5)
root.right.right = Node(6)
if isfoldable(root):
    print "yes"
else:
    print "no"
