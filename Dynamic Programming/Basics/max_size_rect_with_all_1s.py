R = int(raw_input("Number of rows: "))
C = int(raw_input("Number of columns: "))

M = [[int(i) for i in raw_input().split()] for j in range(R)]


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

def max_rectangle_ones(M,R,C):
	result = max_area_rectangle(M[0])
	for i in range(1,R):
		for j in range(0,C):
			if M[i][j] == 1:
				M[i][j] += M[i-1][j]
		result = max(result, max_area_rectangle(M[i]))
	return result

print max_rectangle_ones(M,R,C)

