class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.data = key

def is_bst(root, l=None, r=None):
	if root is None:
		return True

	if l is not None and root.data < l.data:
		return False

	if r is not None and root.data > r.data:
		return False

	return is_bst(root.left, l, root) and is_bst(root.right, root, r)
'''
Time Complexity: O(n)
Auxiliary Space : O(1) if Function Call Stack size is not considered, otherwise O(n)
'''
'''
For iterative, do inorder traversal and see if prev > current.
'''

root = Node(10)
root.left = Node(10)
root.right = Node(19)
root.left.left = Node(-5)
root.right.left = Node(17)
root.right.right = Node(21)

print is_bst(root)