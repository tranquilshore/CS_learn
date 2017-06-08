class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.data = key

#Time complexity of this solution is O(n + m)
def identical_iterative(root1, root2):
    if root1 is None and root2 is None:
        return True
    if root1 is None or root2 is None:
        return False
    
    q1 = []
    q2 = []
    
    q1.append(root1)
    q2.append(root2)
    
    while q1 and q2:
        node1 = q1[0]
        node2 = q2[0]
        
        if node1.data != node2.data:
            return False
        
        q1.pop(0)
        q2.pop(0)
        
        if node1.left and node2.left:
            q1.append(node1.left)
            q2.append(node2.left)
        elif node1.left or node2.left:
            return False
        
        if node1.right and node2.right:
            q1.append(node1.right)
            q2.append(node2.right)
        elif node1.right or node2.right:
            return False
    return True

#time complexity will be according to the tree with lesser number of nodes
def identical_recursive(root1, root2):
    if root1 is None and root2 is None:
        return True
    if root1 is not None and root2 is not None:
        return root1.data == root2.data and identical_recursive(root1.left, root2.left) and identical_recursive(root1.right, root2.right)
    return False
        
        
root1 = Node(1)
root1.left = Node(2)
root1.right = Node(3)
root1.left.left = Node(4)
root1.left.right = Node(5)

root2 = Node(1)
root2.left = Node(2)
root2.right = Node(3)
root2.left.left = Node(4)
root2.left.right = Node(5)

if identical_recursive(root1, root2):
    print "Yes"
else:
    print "No"