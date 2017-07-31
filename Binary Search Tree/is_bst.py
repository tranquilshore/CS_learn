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

#using inorder traversal
def isbst(root):
	if root:
		if !isbst(root.left):
			return False
		if prev != None and root.data <= prev.data:
			return False

		prev = root

		return isbst(root.right)
	return True

#static variable
isbst.prev = None