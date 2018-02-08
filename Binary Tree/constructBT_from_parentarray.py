class Node:
    # A constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def maketree(a):
    d = {}
    n = len(a)

    for i in range(n):
        if d.get(i) is None:
            d[i] = Node(i)
        if d.get(a[i]) is None:
            x = Node(a[i])
            x.left = d[i]
            d[a[i]] = x
        else:
            if d[a[i]].left is None:
                d[a[i]].left = d[i]
            else:
                d[a[i]].right = d[i]
    return d[-1].left

def inorder(root):
    if root is not None:
        inorder(root.left)
        print root.data,
        inorder(root.right)

a = [-1, 0, 0, 1, 1, 3, 5]

root = maketree(a)
inorder(root)