s1 = str(raw_input("Enter s1: "))
s2 = str(raw_input("Enter s2: "))
R = len(s1)
C = len(s2)
LCS = [[0 for i in range(C+1)] for j in range(R+1)]

def lcs(s1, s2):
	for i in range(1, R+1):
		for j in range(1, C+1):
			if s1[i-1] == s2[j-1]:
				LCS[i][j] = LCS[i-1][j-1] + 1
			else:
				LCS[i][j] = max(LCS[i-1][j], LCS[i][j-1])
	return LCS[R][C]
print lcs(s1,s2)

#to print the LCS itself
R = len(s1)
C = len(s2)

index = LCS[R][C]
subseq = [""]*(index+1)
subseq[index] = "\0"

i = R
j = C

while i > 0 and j >0 :
	if s1[i-1] == s2[j-1]:
		subseq[index-1] = s1[i-1]
		i -= 1
		j -= 1
		index -= 1
	elif LCS[i-1][j] > LCS[i][j-1]:
		i -= 1
	else:
		j -= 1
print subseq