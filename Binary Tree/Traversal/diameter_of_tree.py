class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.data = key

def height_r(root):
    if root is None:
        return 0
    else:
        left_h = height_r(root.left)
        right_h = height_r(root.right)
        if left_h > right_h:
            return left_h + 1
        else:
            return right_h + 1
        

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
print height_r(root)