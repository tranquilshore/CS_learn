class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.data = key

        
def toptoleaf_sum_check(current, parent, givensum, flag):
    s = []
    while current:
        s.append(current)
        current = parent[current]
    sum_ = 0
    while s:
        current = s.pop()
        sum_ += current.data
    
    if sum_ == givensum:
        flag = True
        
        
        
#doing with iterative preorder, we need parent info while doing this
def roottoleaf_i(root, givensum, flag):
    if root is None:
        return
    s = []
    s.append(root)
    parent = {}
    parent[root] = None
    while s:
        current = s.pop()
        if current.left is None and current.right is None:
            toptoleaf_sum_check(current, parent, givensum, flag)
        
        if current.right is not None:
            parent[current.right] = current
            s.append(current.right)
        
        if current.left is not None:
            parent[current.left] = current
            s.append(current.left)

        
givensum = 7
flag = False
        
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
roottoleaf_i(root, givensum, flag)

if flag == True:
    print "yes"
else:
    print "no"