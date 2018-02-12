import sys
class Node:
    # A constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def maxpathsumleaves(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return root.data

    ls = maxpathsumleaves(root.left)
    rs = maxpathsumleaves(root.right)

    if root.left is not None and root.right is not None:
        maxpathsumleaves.res = max(maxpathsumleaves.res,ls+rs+root.data)
        return max(ls,rs)+root.data

    if root.left is None:
        return rs+root.data
    else:
        return ls+root.data

maxpathsumleaves.res = -sys.maxint-1

root = Node(-15)
root.left = Node(5)
root.right = Node(6)
root.left.left = Node(-8)
root.left.right = Node(1)
root.left.left.left = Node(2)
root.left.left.right = Node(6)
root.right.left = Node(3)
root.right.right = Node(9)
root.right.right.right= Node(0)
root.right.right.right.left = Node(4)
root.right.right.right.right = Node(-1)
root.right.right.right.right.left = Node(10)

maxpathsumleaves(root)
print maxpathsumleaves.res
