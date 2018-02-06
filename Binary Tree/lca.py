# O(n) solution to find LCS of two given values n1 and n2
class Node:
    # Constructor to create a new binary node
    def __init__(self, key):
        self.key =  key
        self.left = None
        self.right = None
    

 
def lca(root,n1,n2):
    if root is None:
        return None

    if root.key == n1 or root.key == n2:
        return root.key

    leftlca = lca(root.left,n1,n2)
    rightlca = lca(root.right,n1,n2)

    if leftlca and rightlca:
        return root.key

    return leftlca if leftlca is not None else rightlca

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.right.left = Node(6)
root.right.right = Node(8)
root.right.right.left = Node(9)

print lca(root,4,3)