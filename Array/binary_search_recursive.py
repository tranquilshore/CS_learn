def binarySearch(arr,l,r,x):
    if r>=l:
        #to prevent integer overflow
        mid = l + (r-l)/2

        if arr[mid] == x :
            return mid
        elif arr[mid] > x:
            return binarySearch(arr,l,mid-1,x)
        else:
            return binarySearch(arr,mid+1,r,x)
    else:
        #element is not present in the array
        return -1

'''
1. time complexity O(logn)
2. space complexity O(logn) for recursive stack
'''
