import sys
def mincost(cost, m, n):
    if m<0 or n<0:
        return sys.maxint
    elif m == 0 and n == 0:
        return cost[m][n]
    else:
        return cost[m][n] + min(mincost(cost, m-1,n-1), mincost(cost, m-1, n), mincost(cost, m, n-1))
    
cost = [[1,2,3],[4,8,2],[1,5,3]]
print mincost(cost, 2,2)