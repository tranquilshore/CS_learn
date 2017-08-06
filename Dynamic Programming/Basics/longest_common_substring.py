s1 = str(raw_input("Enter S1: "))
s2 = str(raw_input("Enter S2: "))

def lcs(s1,s2):
	R = len(s1)
	C = len(s2)
	LCS = [[0 for i in range(C+1)] for j in range(R+1)]
	result = 0

	for i in range(1, R+1):
		for j in range(1, C+1):
			if s1[i-1] == s2[j-1]: 
				LCS[i][j] = LCS[i-1][j-1] + 1
				result = max(result, LCS[i][j]) 
			else:
				LCS[i][j] = 0

	return result

print lcs(s1,s2)

