class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.data = key
        
def print_leaf_nodes(root):
    if root:
        print_leaf_nodes(root.left)
        
        if root.left is None and root.right is None:
            print root.data,
        
        print_leaf_nodes(root.right)
        
def print_left_boundary(root):
    if root:
        if root.left:
            print root.data,
            print_left_boundary(root.left)
        elif root.right:
            print root.data,
            print_left_boundary(root.right)
        
        #do nothing if its a leaf node
        
def print_right_boundary(root):
    if root:
        if root.right:
            print_right_boundary(root.right)
            print root.right,
        elif root.left:
            print_right_boundary(root.left)
            print root.left,
        #do nothing if its a leaf node

def print_boundary(root):
    if root:
        print root.data,
        print_left_boundary(root.left)
        
        print_leaf_nodes(root.left)
        print_leaf_nodes(root.right)
        
        print_right_boundary(root.right)
        
              
        
root = Node(20)
root.left = Node(8)
root.left.left = Node(4)
root.left.right = Node(12)
root.left.right.left =  Node(10)
root.left.right.right = Node(14)
root.right = Node(22)
root.right.right = Node(25)
print_boundary(root)
