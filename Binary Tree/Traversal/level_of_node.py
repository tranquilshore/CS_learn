class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.data = key

def level_of_node(root, k):
    if root is None:
        return
    q = []
    q.append(root)
    height = 0
    while True:
        node_c = len(q)
        if node_c == 0:
            return False
        height += 1
        while node_c > 0:
            current = q[0]
            if current.data == k:
                return height
            q.pop(0)
            if current.left is not None:
                q.append(current.left)
            if current.right is not None:
                q.append(current.right)
            node_c -= 1
        
        
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print level_of_node(root, 5)
