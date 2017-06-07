class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
    
#recursive
def height(node):
    if node is None:
        return 0
    else:
        left_h = height(node.left)
        right_h = height(node.right)
        
        if left_h > right_h:
            return left_h + 1
        else:
            return right_h + 1
#iterative    
def i_height(root):
    if root is None:
        return 0
    q = []
    q.append(root)
    height = 0
    
    while True:
        node_count = len(q)
        if node_count == 0:
            return height
        height += 1
        
        while node_count > 0:
            node = q[0]
            q.pop(0)
            if node.left is not None:
                q.append(node.left)
            if node.right is not None:
                q.append(node.right)
            node_count -= 1

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
#root.left.left.left = Node(6)

print i_height(root)
