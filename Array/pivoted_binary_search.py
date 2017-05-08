#pivot element is always the one who's next element is than itself, we can use it to apply binary search

def pivotSearch(a,low,high):
    if low>high:
        return -1
    if low == high:
        return low
    mid = low + (high-low)/2
    if mid < high and a[mid]>a[mid+1]:
        return mid
    if mid > low and a[mid] <a[mid-1]:
        return mid-1
    if a[low] <= a[mid]:
        return pivotSearch(a,mid+1,high)
    return pivotSearch(a,low,mid-1)

def pivotedBinarySearch(a,size,key):
    pivot = pivotSearch(a,0,size-1)
    #not rotated at all
    if pivot == -1:
        return binarySearch(a,0,size-1,key)
    
    if a[pivot] == key:
        return pivot
    if a[0] <= key:
        return binarySearch(a,0,pivot-1,key)
    return binarySearch(a,pivot+1,size-1,key)

'''
Time complexity: O(logn)
'''

    