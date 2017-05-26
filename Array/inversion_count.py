#time complexity of this method is O(n^2)
def naive_inversion_count(a):
    n = len(a)
    inv_count = 0
    for i in range(n-1):
        for j in range(i+1, n):
            if a[i] > a [j]:
                inv_count += 1
    return inv_count
#time complexity of this method is O(nlogn)
def inversion_count(a, temp, left, right):
    inv_count = 0
    if right > left:
        mid = (right + left)/2
        #Inversion count will be sum of inversions in left-part, right-part and number of inversions in merging
        inv_count = inversion_count(a, temp, left, mid)
        inv_count += inversion_count(a, temp, mid+1, right)
        #merging two parts
        inv_count += merge(a, temp,left, mid+1, right)
    return inv_count

def merge(a, temp, left, mid, right):
    inv_count = 0
    i = left #left subarray
    j = mid #right subarray
    k = left #resultant merged subarray
    
    while i <= mid -1 and j <= right:
        if a[i] <= a[j]:
            temp[k] = a[i]
            k += 1
            i += 1
        else:
            temp[k] = a[j]
            k += 1
            j += 1
            
            inv_count = inv_count + mid - 1
            
    while i <= mid-1:
        temp[k] = a[i]
        k += 1
        i += 1
    while j <= right:
        temp[k] = a [j]
        k += 1
        j += 1
    
    for i in range(left,right+1):
        a[i] = temp[i]
        
    return inv_count


a = [1, 20, 6, 4, 5]
t = [None]*(len(a))

print inversion_count(a, t, 0, len(a) - 1)
