class Node:
    # A constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
def kdistancedownnodes(root,k):
    if root is None or k < 0:
        return

    if k == 0:
        print root.data
        return

    kdistancedownnodes(root.left,k-1)
    kdistancedownnodes(root.right,k-1)

def kdistancenodes(root,target,k):
    if root is None:
        return -1

    if root == target:
        kdistancedownnodes(root,k)
        return 0
    #dl is distance of root's left child from target
    dl = kdistancenodes(root.left,target,k)
    if dl != -1:
        if dl+1 == k:
            print root.data
        else:
            kdistancedownnodes(root.right, k-dl-2)
        return 1+dl

    #doing the same for the right subtree
    dr = kdistancenodes(root.right, target, k)
    if dr != -1:
        if dr+1 == k:
            print root.data
        else:
            kdistancedownnodes(root.left, k-dr-2)
        return 1+dr
    return -1

root = Node(1)
root.left = Node(20)
root.right = Node(2)

root.left.left = Node(8)
root.left.right = Node(22)

root.left.left.left = Node(4)
root.left.left.right = Node(12)

root.left.left.right.left = Node(10)
root.left.left.right.right = Node(14)

target = root.left.left

kdistancenodes(root,target,2)

