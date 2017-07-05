class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.data = key
        
def increment(root, diff):
    if root.left is not None:
        root.left.data += diff
        #recursively call to fix the descendants of left node
        increment(root.left, diff)
    elif root.right is not None:
        root.right.data += diff
        increment(root.right, diff)
        
#point is to traverse the tree in postorder
def converttree(root):
    left_data = 0
    right_data = 0
    
    if root is None or (root.left == None and root.right is None):
        return
    else:
        converttree(root.left)
        converttree(root.right)
        
        if root.left is not None:
            left_data = root.left.data
        if root.right is not None:
            right_data = root.right.data
        
        diff = left_data + right_data - root.data
        
        if diff > 0:
            root.data += diff
        if diff < 0:
            increment(root, -diff)
            
#O(n)   
def tosumtree(root):
    if root is None:
        return 0
    old_val = root.data
    root.data = tosumtree(root.left) + tosumtree(root.right)
    return root.data + old_val

def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print root.data,
    inorder(root.right)

root = Node(50)
root.left = Node(7)
root.right = Node(2)
root.left.left = Node(3)
root.left.right = Node(5)
root.right.left = Node(1)
root.right.right = Node(30)
converttree(root)
inorder(root)
'''
Time Complexity: O(n^2), Worst case complexity is for a skewed tree such that nodes are in decreasing order from root to leaf.

'''