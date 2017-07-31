def print_sorted(a, start, end):
	if start > end:
		return

	#left subtree
	print_sorted(a, start*2 + 1, end)
	
	#print root
	print a[start]

	#right subtree
	print_sorted(a, start*2 + 2, end)

#Time Complexity: O(n)