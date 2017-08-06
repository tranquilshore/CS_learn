'''
can be solved:
1. find LCS of original and sorted array : O(n^2)
2. DP solution : O(n^2)
3. Binary search solution or patience sort : O(nlogn)
Gonna do the 3rd one and 2nd one
'''
import math
def LIS(a):
	parent = [0]*1000
	insub = [0]*1000
	length = 0
	for i in range(0,len(a)):
		low = 1
		high = length
		while low <= high:
			mid = int(math.ceil((low+high)/2))
			if a[insub[mid]] < a[i]:
				low = mid+1
			else:
				high = mid-1
		pos = low
		#append or replace
		insub[pos] = i
		#updating parent
		parent[i] = insub[pos-1]
		if pos > length:
			length = pos
	return length

def LIS_dp(a):
	n = len(a)
	LIS = [1]*n 

	for i in range(0,n):
		for j in range(0,i):
			if a[j] < a[i]:
				LIS[i] = max(LIS[i], LIS[j]+1)
	return max(LIS)


a = [10,22,9,33,21,50,41,60,80]
print LIS_dp(a)


