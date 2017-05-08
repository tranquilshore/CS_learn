'''
formula:

if j>= coin[i]:
    T[i][j] = T[i-1][j] + T[i][j-coin[i]]
else:
    T[i][j] = T[i-1][j]

'''

def coin_change(coin,m,n):
    table = [0 for i in range(n+1)]
    table[0] = 1
    for i in range(0,m):
        for j in range(coin[i], n+1):
            table[j] += table[j - coin[i]]
    return table[n]

coin = [1,2,3]
m = len(coin)
n = 4
print coin_change(coin, m,n)
'''
time complexity O(mn)
'''