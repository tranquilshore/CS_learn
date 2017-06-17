class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.data = key

ans = []        

def peek(stack):
    if len(stack)>0:
        return stack[-1]
    return None

#using single stack
def postorder_iterative(root):
    if root is None:
        return
    s = []
    while True:
        while root:
            if root.right is not None:
                s.append(root.right)
            s.append(root)
            root = root.left
        root = s.pop()
        if root.right is not None and peek(s) == root.right:
            s.pop()
            s.append(root)
            root = root.right
        else:
            ans.append(root.data)
            root = None
        if len(s) <= 0 :
            break
        
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
postorder_iterative(root)
print ans