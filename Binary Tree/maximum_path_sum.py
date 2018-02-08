import sys
class Node:
    # A constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def maxpathsum(root):
    if root is None:
        return 0

    l = maxpathsum(root.left)
    r = maxpathsum(root.right)

    maxlr = max(l,r)
    maxsingle = max(maxlr+root.data,root.data)
    maxtop = max(maxsingle,l+r+root.data)

    maxpathsum.res = max(maxpathsum.res,maxtop)
    return maxsingle

maxpathsum.res = -sys.maxint -1
root = Node(10)
root.left = Node(2)
root.right   = Node(10)
root.left.left  = Node(20)
root.left.right = Node(1)
root.right.right = Node(-25)
root.right.right.left   = Node(3)
root.right.right.right  = Node(4)

maxpathsum(root)

print "Max path sum is ", maxpathsum.res

