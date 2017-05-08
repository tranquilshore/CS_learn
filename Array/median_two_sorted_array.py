def median(a1[], a2[], n):
    if n <= 0:
        return -1
    if n == 1:
        return (a1[0] + a2[0])/2
    if n == 2:
        return (max(a1[0], a2[0]) + min(a1[1], a2[1]))/2
    
    m1 = median(a1, n)
    m2 = median(a2, n)
    
    if m1 == m2:
        return m1
    
    if m1 < m2:
        if n%2 == 0:
            return median(a1+n/2 - 1, a2, n - n/2 + 1)
        return median(a1 + n/2, a2, n-n/2)
    
    if n%2 == 0:
        return median(a2 + n/2 - 1, a1, n - n/2 + 1)
    return median(a2 + n/2, a1, n-n/2)

'''
time complexity: O(logn)
divide and conquer
'''