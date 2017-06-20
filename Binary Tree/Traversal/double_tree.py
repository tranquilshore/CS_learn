'''
Recursively convert the tree to double tree in postorder fashion. For each node, first convert the left subtree of the node, then right subtree, finally create a duplicate node of the node and fix the left child of the node and left child of left child.
'''

class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.data = key

def doubletree(root):
    if root is None:
        return
    doubletree(root.left)
    doubletree(root.right)
    
    oldleft = node.left
    node.left = Node(node.data)
    node.left.left = oldleft
            
        
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)