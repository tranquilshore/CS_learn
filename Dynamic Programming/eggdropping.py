'''
eggdrop(n,k) = 1 + min{max(eggdrop(x-1,n-1), eggdrop(k-x,n))}

'''

import sys

def eggdropping_recursive(n,k):
	if k == 1 or k == 0:
		return k

	if n == 1:
		return k

	min_val = sys.maxint

	for x in range(1,k+1):
		res = max(eggdropping_recursive(n-1,x-1), eggdropping_recursive(n,k-x))
		if res < min_val :
			min_val = res 

	return min_val + 1 

def eggdropping_dp(n,k):
	eggdrop = [[None]*(k+1) for i in range(n+1)]
	for i in range(1,n+1):
		eggdrop[i][1] = 1
		eggdrop[i][0] = 0

	for j in range(1,k+1):
		eggdrop[1][j] = j

	for i in range(2,n+1):
		for j in range(2,k+1):
			eggdrop[i][j] = sys.maxint
			for x in range(1,j+1):
				res = 1 + max(eggdrop[i-1][x-1], eggdrop[i][j-x])
				if res < eggdrop[i][j]:
					eggdrop[i][j] = res
'''
for dp:
Time Complexity: O(nk^2)
Auxiliary Space: O(nk)
'''

	return eggdrop[n][k]

print eggdropping_dp(2,10)

