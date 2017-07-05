class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.data = key

'''
Tree S is a subtree of T if both inorder and preorder traversals of S are substrings(can also be in O(n) using KMP string matching algorithm) of inorder and preorder traversals of T respectively.
'''
    
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.left.left = Node(7)