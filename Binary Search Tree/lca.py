def lca(root, n1, n2):
	while root is not None:
		if root.data > n1 and root.data>n2:
			root = root.left
		elif root.data < n1 and root.data < n2:
			root = root.right

		else:
			break
	return root

#Time complexity of above solution is O(h) where h is height of tree