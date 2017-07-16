class Node:
    def __init__(self,key):
        self.data = key
        self.left = None
        self.right = None
        
def insert(root,key):
    if root is None:
        return Node(key)
    
    if key < root.data:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root

def presuc(root, key):
    if root is None:
        return 
    
    if root.data = key:
        if root.left is not None:
            tmp = root.left
            while tmp.right:
                tmp = tmp.right
            presuc.pre = tmp
        
        if root.right is not None:
            tmp = root.right
            while tmp.left:
                tmp = tmp.left
            presuc.suc = tmp
            
        return




root = None
root = insert(root, 50)
insert(root,30)
insert(root,20)
insert(root,40)
insert(root,70)
insert(root,60)
insert(root,80)

#static variables of the function presuc
presuc.pre = None
presuc.suc = None

presuc(root, key)
