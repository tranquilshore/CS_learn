def editdistIDM(str1, str2, m, n):
    dp = [[None]*(n+1) for i in range(m+1)]
    
    for i in range(m+1):
        for j in range(n+1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            
            elif str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]
                
            else:
                dp[i][j] = 1 + min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1])
                
    return dp[m][n]

str1 = "sunday"
str2 = "saturday"

print editdistIDM(str1, str2, len(str1), len(str2))

'''
1. time complexity: O(mn)
2. applications: to display all the words in a dictionary that are near proximity to a given word/incorrectly spelled word
3. apache lucene
'''