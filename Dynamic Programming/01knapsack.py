'''
formula:

if j<wt[i]:
    T[i][j] = T[i-1][j] 
else:
    T[i][j] = max{ val[i] + T[i-1][j-wt[i]] , T[i-1][j]}
    
    -> j-wt[i] weight remain after selecting i

'''

def knapsack(W, wt, val, n):
    k = [[None]*(W+1) for i in range(n+1)]
    
    for i in range(n+1):
        for j in range(W+1):
            if i == 0 or j == 0:
                k[i][j] = 0
            elif wt[i-1] <= j:
                k[i][j] = max(val[i-1] + k[i-1][j-wt[i-1]], k[i-1][j])
            else:
                k[i][j] = k[i-1][j]
    return k[n][W]

val = [60, 100, 120]
wt = [10, 20, 30]
W = 50

n = len(val)
print knapsack(W, wt, val, n)

'''
time complexity:
O(nW)
'''