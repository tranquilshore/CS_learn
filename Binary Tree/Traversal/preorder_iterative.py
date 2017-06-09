class Node:
	def __init__(self, key):
		self.left = None
		self.right = None
		self.data = key

def preorder_iterative(root):
	if root is None:
		return

	s = []
	s.append(root)

	while s:
		node = s.pop()
		print node.data,

		if node.right:
			s.append(node.right)
		if node.left:
			s.append(node.left)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
print preorder_iterative(root)
