#recursive
def r_fib(n):
	if n <= 1:
		return n
	return r_fib(n-1) + r_fib(n-2)

#memoization(top down) : similar to recursion
lookup = [None]*101
def m_fib(n, lookup):
	if n == 1 or n == 0:
		lookup[n] = n

	#if not calculated then calculate it
	if lookup[n] == None:
		lookup[n] = m_fib(n-1, lookup) + m_fib(n-2, lookup)

	return lookup[n]

#tabulation(bottom up)
def t_fib(n):
	#array declaration
	f = [0]*(n+1)

	#base case
	f[1] = 1

	for i in range(2, n+1):
		f[i] = f[i-1] + f[i-2]

	return f[n]




