class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

def lca(root,n1,n2):
    if root is None:
        return None

    if root.data == n1 or root.data == n2:
        return root

    leftlca = lca(root.left,n1,n2)
    rightlca = lca(root.right,n1,n2)

    if leftlca and rightlca:
        return root

    return leftlca if leftlca is not None else rightlca

def levelofnode(root,k,level):
    if root is None:
        return -1
    if root.data == k:
        return level
    l = levelofnode(root.left,k,level+1)
    if l != -1:
        return l
    return levelofnode(root.right,k,level+1)

def finddistance(root,n1,n2):
    lca_val = lca(root,n1,n2)

    d1 = levelofnode(lca_val,n1,0)
    d2 = levelofnode(lca_val,n2,0)

    return d1 + d2

root = Node(10)
root.left = Node(5)
root.right = Node(11)
root.left.left = Node(4)
root.left.right = Node(8)
root.left.right.left = Node(16)
root.right.right = Node(13)

print finddistance(root,5,11)