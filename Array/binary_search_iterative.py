def binarySearch(arr, l, r, x):
    while l<= r:
        mid = l + (r-l)/2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            l = mid+1
        else:
            r = mid-1
    #if element is not present
    return -1

'''
works only for sorted array 
1. time complexity O(logn)
2. space complexity O(1)
'''
