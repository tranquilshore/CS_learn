class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.data = key
        
def is_complete_tree(root):
    if root is None:
        return
    
    q = []
    q.append(root)
    
    flag = False
    
    while len(q) > 0:
        tmp = q[0]
        q.pop(0)
        
        if tmp.left:
            if flag == True:
                return False
            q.append(tmp.left)
        else:
            flag = True
            
        if tmp.right:
            if flag == True:
                return False
            q.append(tmp.right)
        else:
            flag = True
    return True
        
root = Node(1)
root.left = Node(2)
root.right = Node(3)
#root.left.left = Node(4)
root.left.right = Node(5)

if is_complete_tree(root):
    print "yes"
else:
    print "no"
    
'''
Time Complexity: O(n) where n is the number of nodes in given Binary Tree

Auxiliary Space: O(n) for queue
'''
