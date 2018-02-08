class Node:
    # A constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def sumtree(root):
    if root is None:
        return 0

    oldval = root.data

    l = sumtree(root.left)
    r = sumtree(root.right)
    root.data = l + r

    return oldval + root.data

def inorder(root):
    if root is not None:
        inorder(root.left)
        print root.data,
        inorder(root.right)
    


root = Node(10)
root.left = Node(-2)
root.right = Node(6)
root.left.left = Node(8)
root.left.right = Node(-4)
root.right.left = Node(7)
root.right.right = Node(5)

sumtree(root)
inorder(root)
