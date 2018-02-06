'''
formula:

if j<wt[i]:
    T[i][j] = T[i-1][j] 
else:
    T[i][j] = max{ val[i] + T[i-1][j-wt[i]] , T[i-1][j]}
    
    -> j-wt[i] weight remain after selecting i

'''
val = [9,9,9,10,6]
wt = [1,2,1,2,1]
W = 3
n = len(val)

k = [[None]*(W+1) for i in range(n+1)]
def knapsack(W, wt, val, n):
    
    for i in range(n+1):
        for j in range(W+1):
            if i == 0 or j == 0:
                k[i][j] = 0
            elif wt[i-1] <= j:
                k[i][j] = max(val[i-1] + k[i-1][j-wt[i-1]], k[i-1][j])
            else:
                k[i][j] = k[i-1][j]
    return k[n][W]


print knapsack(W, wt, val, n)
tmplist = []

for i in range(len(val),-1,-1):
    if k[i][W] > k[i-1][W]:
        tmplist.append(wt[i-1])
        W -= wt[i-1]
print tmplist

'''
time complexity:
O(nW)
'''