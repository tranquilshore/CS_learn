def quicksort(A, si, ei):
    if si<ei:
        pi = partition(A, si, ei) # n
        quicksort(A,si,pi-1)# T(n/2)
        quicksort(A,pi+1,ei)# T(n/2)

def partition(A, si, ei):
    x = A[si]
    i = si -1
    for j in range(si,ei):
        if A[j]<=x:
            i+=1
            #swap operation
            A[i], A[j] = A[j], A[i]
        A[i+1], A[ei] = A[ei], A[i+1]
    return i+1

'''
1. best case time complexity O(nlogn) : T(n) = T(n/2) + cn
2. worst cast is O(n^2) : can be avaided by randomized version of quick sort T(n) = T(n-1) + cn
'''
