#m+n[] array of size m+n, n[] array of size n
#1. move m elements of m+n to the end
#2. start from n elements of m+n and first element of n and merge them into m+n.

def moveToEnd(a,size):
    j = size-1
    for i in range(size-1,-1,-1):
        if mplusn[i] is not NA:
            mplusn[j] = mplusn[i]
            j--

def merge(mplusn,N,m,n):
    i = n
    j = 0
    k = 0
    while k < m+n:
        if (i < m+n and mplusn[i] <= N[j]) or j == n:
            mplusn[k] = mplusn[i]
            k++
            i++
        else:
            mplus[k] = N[j]
            k++
            j++
        
'''
Time complexity: O(m+n)
'''