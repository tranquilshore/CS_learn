class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.data = key
        
def print_ancestor(root, target):
    if root == None:
        return False
    if root.data == target:
        return True
    if print_ancestor(root.left, target) or print_ancestor(root.right, target):
        print root.data,
        return True
    return False
    
    
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.left.left = Node(7)

print_ancestor(root, 7)

'''
time complexity is O(n)
'''