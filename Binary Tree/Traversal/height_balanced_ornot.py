class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.data = key

def isbalanced(root):
    if root is None:
        return 0
    left = isbalanced(root.left)
    right = isbalanced(root.right)
    if left < 0 or right < 0 or abs(left - right) > 1:
        return -1
    return max(left, right) + 1
        
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.left.left = Node(6)
root.left.right = Node(5)

if isbalanced(root) >= 0:
    print "yes"
else:
    print "no"
