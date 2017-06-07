class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.data = key

#recursive O(n^2)
def height(root):
    if root is None:
        return 0
    else:
        left_h = height(root.left)
        right_h = height(root.right)
        if left_h > right_h:
            return left_h + 1
        else:
            return right_h + 1

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
        
def printgivenlevel(root, level):
    if root is None:
        return
    if level == 1:
        print root.data,
    elif level > 1:
        printgivenlevel(root.left, level-1)
        printgivenlevel(root.right, level-1)

def printlevelorder(root):
    h = height(root)
    for i in range(1, h+1):
        printgivenlevel(root, i)
        
#iterative O(n)

def levelordertraversal(root):
    if root is None:
        return
    q = []
    q.append(root)
    while len(q) > 0:
        print q[0].data,
        node = q.pop(0)
        
        if node.left is not None:
            q.append(node.left)
        if node.right is not None:
            q.append(node.right)

        
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print levelordertraversal(root)
