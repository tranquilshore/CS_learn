class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.data = key
        
        
def printtoptobottom(current, parent):
    s = []
    while current:
        s.append(current)
        current = parent[current]
    
    while s:
        current = s.pop()
        print current.data,
    print "\n"
#done with iterative preorder traversal which is done using stack       
def roottoleaf_iterative(root):
    if root is None:
        return
    s = []
    s.append(root)
    parent = {}
    parent[root] = None
    
    while s:
        current = s.pop()
        if current.left is None and current.right is None:
            printtoptobottom(current, parent)
        if current.right:
            parent[current.right] = current
            s.append(current.right)
            
        if current.left:
            parent[current.left] = current
            s.append(current.left)

#recursive
def printpath(root):
    path = [0]*1000
    roottoleaf_recursive(root, path, 0)
    
def printarray(path, pathlen):
    for i in range(pathlen):
        print path[i],
    print "\n"
                    
def roottoleaf_recursive(root, path, pathlen):
    if root is None:
        return
    path[pathlen] = root.data
    pathlen += 1
    
    if root.left is None and root.right is None:
        printarray(path, pathlen)
    else:
        roottoleaf_recursive(root.left, path, pathlen)
        roottoleaf_recursive(root.right, path, pathlen)
            

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

#roottoleaf_iterative(root)
printpath(root)

