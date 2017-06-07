class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key

#in case of BST, it gives nodes in increasing order
def printInorder(root):

    if root:
        # First recur on left child
        printInorder(root.left)
        # then print the data of node
        print(root.val),
        # now recur on right child
        printInorder(root.right)

#it is used to delete the tree, also used to get postfix expression of an expression tree, Reverse Polish Notation used for implementing stack machines, JVM is one of them
def printPostorder(root):

    if root:
        # First recur on left child
        printPostorder(root.left)
        # the recur on right child
        printPostorder(root.right)
        # now print the data of node
        print(root.val),

#it is used to create a copy of the tree, also used to get the prefix expression of an expression tree
def printPreorder(root):

    if root:
        # First print the data of node
        print(root.val),
        # Then recur on left child
        printPreorder(root.left)
        # Finally recur on right child
        printPreorder(root.right)
        
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

printPreorder(root)
'''
pre-/postfix notation is easier to parse for a machine. The big advantage in pre-/postfix notation is that there never arise any questions like operator precedence.
time complexity O(n)
space complexity O(n) function call stack

'''