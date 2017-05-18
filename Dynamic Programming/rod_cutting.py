'''
if (j >= i):
	T[i][j] = max(T[i-1][j], val[i]+T[i][j-i])
else:
	T[i][j] = T[i-1][j]
'''

