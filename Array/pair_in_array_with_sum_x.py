#method 1: using sorting gives O(nlogn)

def pairInArrayWithSumX(a, arr_size, pair_sum):
    quicksort(a,0,arr_size-1)
    l = 0
    r = arr_size - 1
    while l<r:
        if (a[l] + a[r] == pair_sum):
            return 1
        elif (a[l] + a[r] < pair_sum):
            l += 1
        else:
             r -= 1
    return 0

#method 2: using hashmap gives O(n) if range O(R) of number is known or given infinite space

max_count = 10000
def pairInArrayWithSumX(a, arr_size, pair_sum):
    bin_hash_map = [0]*max_count
    for i in range(0,arr_size):
        temp = pair_sum - a[i]
        if (temp > 0 and bin_hash_map[temp] = 1):
            return 1
        bin_hash_map[a[i]] = 1
    return 0