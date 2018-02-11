class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.data = key

def levelordertraversal(root):
    if root is None:
        return
    q = []
    q.append(root)

    while True:
        nodecount = len(q)
        if nodecount == 0:
            break
        while nodecount > 0:
            print q[0].data,
            current = q.pop(0)

            if current.left is not None:
                q.append(current.left)
            if current.right is not None:
                q.append(current.right)
            nodecount -= 1
        print "\n"
    return

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.right.left = Node(6)
root.right.right = Node(7)
root.right.right.right = Node(8)

print levelordertraversal(root)