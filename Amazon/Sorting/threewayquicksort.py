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
1. best case time complexity O(nlog(2)n) : T(n) = T(n/2) + cn
2. worst cast is O(n^2) : can be avaided by randomized version of quick sort T(n) = T(n-1) + cn
'''

'''
can also be done using 3 way paritioning which uses Dutch national flag algorithm
time complexity O(nlog(3)n)
'''
#Dutch national flag algorithm which sorts array of 0,1,2's

def dnf(a):
    lo,mid = 0,0
    hi = len(a) - 1

    while mid <= hi:
        if a[mid] == 0:
            a[lo],a[mid] = a[mid],a[lo]
            lo += 1
            mid += 1
        elif a[mid] == 1:
            mid += 1
        else:
            a[mid],a[hi] = a[hi], a[mid]
            hi -= 1
    return a

# quick sort using three way partitioning 
def three_way_partition(a, low, high, i, j):
    mid = low
    pivot = a[high]

    while mid <= high:
        if a[mid] < pivot:
            a[low], a[mid] = a[mid], a[low]
            low += 1
            mid += 1
        elif a[mid] == pivot:
            mid += 1
        elif a[mid] > pivot:
            a[mid], a[high] = a[high], a[mid]
            high -= 1
    i = low - 1
    j = high
    return i,j

def three_way_quicksort(a, low, high):
    if low >= high:
        return
    i, j = None, None

    i, j = three_way_partition(a, low, high, i, j)

    three_way_quicksort(a, low, i)
    three_way_quicksort(a, j, high)



