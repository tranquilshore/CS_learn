class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.data = key

        
def print_k_dist_nodes(current, parent, k):
    s = []
    while current:
        s.append(current)
        current = parent[current]
    if k <= len(s):
        count = 0
        while s:
            current = s.pop()
            if count == k:
                print current.data,
            count += 1
    return
                   
        
def root_to_k_nodes(root, k):
    if root is None:
        return
    s = []
    s.append(root)
    parent = {}
    parent[root] = None
    while s:
        current = s.pop()
        if current.left is None and current.right is None:
            print_k_dist_nodes(current, parent, k)
        if current.right:
            parent[current.right] = current
            s.append(current.right)
        if current.left:
            parent[current.left] = current
            s.append(current.left)
            
def printkdistant_r(root, k):
    if root is None:
        return
    if k == 0:
        print root.data
    else:
        printkdistant_r(root.left, k-1)
        printkdistant_r(root.right, k-1)
            
        
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
printkdistant_r(root, 1)
