class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.data = key


#diameter will be anyone of the following:
#1. diameter of left subtree
#2. diameter of right subtree
#3. height of left subtree + height of right subtree + 1

#optimized solution O(n)
def diameter_height(root):
    if root is None:
        return 0,0
    ld, lh = diameter_height(root.left)
    rd, rh = diameter_height(root.right)
    return max(lh + rh + 1, ld, rd), 1+max(lh, rh)

def diameter(root):
    d, _ = diameter_height(root)
    return d
    

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print diameter(root)