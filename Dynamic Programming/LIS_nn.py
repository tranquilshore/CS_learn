def LIS(a):
    n = len(a)
    #LIS at each index is 1 at least
    lis = [1]*n
    
    for i in range(1,n):
        for j in range(0,i):
            if a[j]<a[i]:
                lis[i] = max(lis[i], lis[j]+1)
                
    return max(lis)

a = [3,4,-1,0,6,2,4]
print LIS(a)
    