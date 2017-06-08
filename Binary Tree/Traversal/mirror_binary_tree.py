class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.data = key
        
def mirror_iterative(root):
    if root is None:
        return
    
    s = []
    s.append(root)
    while s:
        current = s.pop()
        
        #swapping
        temp = current.right
        current.right = current.left
        current.left = temp
        
        #important as right will enter the stack first
        if current.right:
            s.append(current.right)
        if current.left:
            s.append(current.left)

def mirror_recursive(root):
    if root is None:
        return
    else:
        mirror_recursive(root.left)
        mirror_recursive(root.right)
        
        temp = root.left
        root.left = root.right
        root.right = temp
        

def inorder(root):
    if root:
        inorder(root.left)
        print root.data,
        inorder(root.right)
        
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

inorder(root)
print "\n"
mirror_iterative(root)
inorder(root)