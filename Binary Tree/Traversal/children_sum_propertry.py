class Node:
	def __init__(self, key):
		self.left = None
		self.right = None
		self.data = key

def childsum_iterative(root):
	if root is None:
		return
	s = []
	s.append(root)
	while s:
		current = s.pop()
		if current.left is not None and current.right is not None:
			if current.data != current.left.data + current.right.data:
				return False
		if current.left is not None and current.right is None:
			if current.data != current.left.data + 0:
				return False
		if current.left is None and current.right is not None:
			if current.data != 0 + current.right.data:
				return False

		if current.right:
			s.append(current.right)
		if current.left:
			s.append(current.left)
	return True

def childsum_recursive(root):
    left_data = 0
    right_data = 0
    if root is None or (root.left is None and root.right is None):
        return 1
    else:
        if node.left is not None:
            left_data = root.left.data
        if node.right is not None:
            right_data = root.right.data
        if root.data == left_data + right_data and childsum_recursive(root.left) and childsum_recursive(root.right):
            return 1
        else:
            return 0


root = Node(10)
root.left = Node(8)
root.right = Node(2)
root.left.left = Node(5)
root.left.right = Node(3)

if childsum_iterative(root):
	print "yes"
else:
	print "No"