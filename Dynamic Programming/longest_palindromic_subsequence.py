'''
if first char == last char:
	L(0,n-1) = L(1,n-2) + 2
else:
	L(0,n-1) = max(L(1,n-1), L(0,n-2))

Time Complexity of lps_dp is O(n^2)
Following is the two step solution that uses LCS.
1) Reverse the given sequence and store the reverse in another array say rev[0..n-1]
2) LCS of the given sequence and rev[] will be the longest palindromic sequence.
This solution is also a O(n^2) solution. 

'''

def lps_recursive(seq, i, j):
	#base case: only 1 character
	if i == j:
		return 1
	#base case: if only 2 characters and both are same
	if seq[i] == seq[j] and i+1 == j:
		return 2
	#if first and last characters matches
	if seq[i] == seq[j]:
		return lps_recursive(seq, i+1, j-1) + 2
	#if first and last character doesn't matches
	return max(lps_recursive(i+1,j), lps_recursive(i,j-1))

def lps_dp(strng):
	n = len(strng)

	L = [[None]*n for i in range(n)]
	for i in range(n):
		L[i][i] = 1
	#ls is the length of substring
	for ls in range(2, n+1):
		for i in range(n-ls+1):
			j = i+ls-1

			if strng[i] == strng[j] and ls == 2:
				L[i][j] = 2

			elif strng[i] == strng[j]:
				L[i][j] = L[i+1][j-1] + 2
			else:
				L[i][j] = max(L[i][j-1], L[i+1][j])
	return L[0][n-1]

seq = "GEEKS FOR GEEKS"
n = len(seq)
print("The length of the LPS is " + str(lps_dp(seq)))
