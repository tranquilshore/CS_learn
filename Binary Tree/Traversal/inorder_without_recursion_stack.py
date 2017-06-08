class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.data = key

        
def morristraversal(root):
    if root is None:
        return
    
    current = root
    while current is not None:
        if current.left is None:
            print current.data,
            current = current.right
        else:
            #finding the inorder predecessor
            pre = current.left
            while pre.right is not None and pre.right != current:
                pre = pre.right
            if pre.right is None:
                pre.right = current
                current = current.left
            else:
                pre.right = None
                print current.data,
                current = current.right
                
        

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print morristraversal(root)