def MIS(a):
	n = len(a)
	mis = [0]*n
	for i in range(n):
		mis[i] = a[i]

	for i in range(n):
		for j in range(i):
			if a[j] < a[i]:
				mis[i] = max(mis[i], mis[j]+a[i])
	return max(mis)
a = [1, 101, 2, 3, 100, 4, 5]
print MIS(a)
