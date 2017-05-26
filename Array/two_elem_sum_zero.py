import sys

#O(n^2)
def minSumPair(a,n):
    min_l = 0
    min_r = 1
    min_sum = a[0] + a[1]
    
    for l in range(n-1):
        for r in range(l+1,n):
            sm = a[l] + a[r]
            if abs(min_sum) > abs(sm):
                min_sum = sm
                min_l = l
                min_r = r
    print a[min_l], a[min_r]
    
#O(nlogn)
def _minSumPair(a,n):
    min_sum = sys.maxint
    l = 0
    r = n-1
    min_l = l
    min_r = n-1
    a.sort()
    while l < r:
        sm = a[l] + a[r]
        if abs(sm) < abs(min_sum):
            min_sum = sm
            mil_l = l
            min_r = r
        if sm < 0:
            l += 1
        else:
            r -= 1
    print a[min_l], a[min_r]
    
    
    
a = [1, 60, -10, 70, -80, 85]
n = len(a)
print _minSumPair(a,n)
