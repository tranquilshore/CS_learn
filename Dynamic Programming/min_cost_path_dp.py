def mincost(cost, m, n):
    dp = [[None]*(m+1) for i in range(n+1)]
    
    dp[0][0] = cost[0][0]
    
    #initializing first column
    for i in range(1,m+1):
        dp[i][0] = dp[i-1][0] + cost[i][0]
        
    #initializing first row
    for i in range(1, n+1):
        dp[0][i] = dp[0][i-1] + cost[0][i]
        
    #rest of the matrix
    for i in range(1, m+1):
        for j in range(1, n+1):
            dp[i][j] = min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j]) + cost[i][j]
            
    return dp[m][n]

cost = [[1, 2, 3],
        [4, 8, 2],
        [1, 5, 3]]

print mincost(cost,2,2)

'''
time complexity: O(mn)
'''