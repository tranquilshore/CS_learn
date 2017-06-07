class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.data = key
        
def leveltraversalbyline(root):
    if root is None:
        return
    q = []
    q.append(root)
    while True:
        node_count = len(q)
        if node_count == 0:
            break
        while node_count > 0 :
            print q[0].data,
            node = q.pop(0)
            if node.left is not None:
                q.append(node.left)
            if node.right is not None:
                q.append(node.right)
            node_count -= 1
        print "\n"
            
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print leveltraversalbyline(root)