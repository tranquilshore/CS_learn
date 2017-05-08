import math
def LIS(arr):
    parent = [0]*100#tracking predecessors of elements of each subsequence
    increasingSub = [0]*100#tracking ends of each increasing subsequence
    #increasingSub[0] = arr[0]
    length = 0#length of longest subsequence
    for i in range(0,len(arr)):
        #binary search
        low = 1
        high = length
        while low <= high:
            mid = math.ceil((low+high)/2)
            mid = int(mid)
            if(arr[increasingSub[mid]] < arr[i]):
                low = mid+1
            else:
                high = mid -1
        pos = low
        #replace or append
        increasingSub[pos] = i
        #update parent for LIS
        parent[i] = increasingSub[pos-1]
        if pos > length:
            length = pos
            
    LIS = [0]*100
    k = increasingSub[length]
    for j in range(length-1,-1,-1):
        LIS[j] = arr[k]
        k = parent[k]
        
    for i in range(0,length):
        print LIS[i]
            
arr = [3,4,-1,0,6,2,3]
LIS(arr)

        