class Node:
    # A constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.pathlen = 0

def findmaxbendsutil(root,direc,bends,maxbends,sofar,len_):
    if root is None:
        return
    #leaf node
    if root.left is None and root.right is None:
        if bends > maxbends[0]:
            maxbends[0] = bends
            len_[0] = sofar
    elif root.left is None:#left child is None
        if direc == 'r':
            findmaxbendsutil(root.right,direc,bends,maxbends,sofar+1,len_)
        else:
            findmaxbendsutil(root.right,'r',bends+1,maxbends,sofar+1,len_)
    elif root.right is None:#right child is None
        if direc == 'l':
            findmaxbendsutil(root.left,direc,bends,maxbends,sofar+1,len_)
        else:
            findmaxbendsutil(root.left,'l',bends+1,maxbends,sofar+1,len_)
    else:#having both left and right child
        if dir == 'l':
            findmaxbendsutil(root.left,direc,bends,maxbends,sofar+1,len_)
            findmaxbendsutil(root.right,'r',bends+1,maxbends,sofar+1,len_)
        else:
            findmaxbendsutil(root.right,direc,bends,maxbends,sofar+1,len_)
            findmaxbendsutil(root.left,'l',bends+1,maxbends,sofar+1,len_)

def findmaxbends(root):
    if root is None:
        return 0
    bends = 0
    maxbends = list()
    maxbends.append(-1)
    len_ = list()
    len_.append(0)

    #call for left subtree
    if root.left:
        findmaxbendsutil(root.left,'l',bends,maxbends,1,len_)
    #call for right subtree
    if root.right:
        findmaxbendsutil(root.right,'r',bends,maxbends,1,len_)
    len_[0] += 1
    return len_[0]

root = Node(10)
root.left = Node(8)
root.right = Node(2)
root.left.left = Node(3)
root.left.right = Node(5)
root.right.left = Node(2)
root.right.left.right = Node(1)
root.right.left.right.left = Node(9)
root.right.left.right.left.right = Node(5)

print findmaxbends(root)
 
