class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.data = key
        
def max_width(root):
    if root is None:
        return 0
    q = []
    q.append(root)
    maxwidth = 0
    
    while q != []:
        node_c = len(q)
        maxwidth = max(maxwidth , node_c)
        while node_c > 0:
            node = q[0]
            q.pop(0)
            if node.left is not None:
                q.append(node.left)
            if node.right is not None:
                q.append(node.right)
            node_c -= 1
    return maxwidth
        

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
print max_width(root)
