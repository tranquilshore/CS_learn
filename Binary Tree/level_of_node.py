class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

def levelofnode(root,k,level):
    if root is None:
        return -1
    if root.data == k:
        return level
    l = levelofnode(root.left,k,level+1)
    if l != -1:
        return l
    return levelofnode(root.right,k,level+1)

root = Node(10)
root.left = Node(5)
root.right = Node(11)
root.left.left = Node(4)
root.left.right = Node(8)
root.left.right.left = Node(16)
root.right.right = Node(13)


print levelofnode(root,8,0)