class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

def sumleftleaves(root,isleft,leftsum):
    if root is None:
        return 0
    if root.left is None and root.right is None and isleft==True:
        leftsum[0] += root.data
    sumleftleaves(root.left,1,leftsum)
    sumleftleaves(root.right,0,leftsum)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

leftsum = [0]
sumleftleaves(root,0,leftsum)
print leftsum[0]