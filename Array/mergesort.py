def merge(a,l,m,r):
    n1 = m-l+1
    n2 = r-m
    
    #temp arrays
    L = [0]*n1
    R = [0]*n2
    
    for i in range(0,n1):
        L[i] = a[l+i]
        
    for j in range(0,n2):
        R[j] = a[m+1+j]
    i = j = 0
    k = l
    
    while l < n1 and j <n2:
        if L[i] <= T[j]:
            a[k] = L[i]
            i += 1
        else:
            a[k] = R[j]
            j += 1
        k += 1
    
    while i < n1:
        a[k] = L[i]
        i += 1
        k += 1
        
    while j < n2:
        a[k] = R[j]
        j += 1
        k += 1
def mergesort(a,l,r):
    if l<r:
        m = l + (r-l)/2
        mergesort(a, l, m)
        mergesort(a, m+1, r)
        merge(a,l,m,r)

'''
1. time complexity : O(nlogn)
2. Space complexity: O(n)
3. stable sort
'''