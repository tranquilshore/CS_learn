A = [6,2,5,4,5,1,6]

def max_area_rectangle(A):
	s = []
	max_area = 0
	i = 0
	n = len(A)
	while i < n:
		if not s or A[s[-1]] <= A[i]:
			s.append(i)
			i += 1
		else:
			top = s.pop()
			if not s:
				val = i
			else:
				val = i - s[-1] - 1
			area_with_top = A[top]*val
			max_area = max(max_area, area_with_top)

	while not not s:
		top = s.pop()
		if not s:
			val = i
		else:
			val = i - s[-1] - 1
		area_with_top = A[top]* val
		max_area = max(max_area, area_with_top)
	return max_area

print max_area_rectangle(A)

