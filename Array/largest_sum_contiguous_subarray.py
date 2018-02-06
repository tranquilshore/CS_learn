#kadane's algorithm
#largest subarray sum will either be the element at the current index or it will be the sum combined the element at  current index with the maximum subarray at the previous index max(X, [M+X]).

def kadane(a, size):
    current_max = global_max = a[0]
    for i in range(1, size):
        current_max = max(a[i], current_max+a[i])
        if current_max > global_max:
            global_max = current_max
    return global_max

'''
Time complexity : O(n)
'''

def kadaneWithIndexes(a,size):
    max_so_far = -sys.maxint -1
    max_ending_here = 0
    start = end = s =0
    for i in range(0,size):
        max_ending_here += a[i]

        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
            start = s
            end = i
        if max_ending_here < 0:
            max_ending_here = 0
            s = i+1

