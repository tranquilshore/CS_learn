class Node:
    def __init__(self,key):
        self.right = None
        self.left = None
        self.data = key
#recursive
def size(root):
    if root is None:
        return 0
    else:
        return size(root.left) + 1 + size(root.right)
        
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print size(root)

'''
can use any other efficient traversal techniques used above.
'''