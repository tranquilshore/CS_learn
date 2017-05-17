'''
DP solution
assumption:
All elements are positive
temp = incl
incl = max(incl, exc + input[i])
exc = temp
'''

def max_sum_sub_nonadj(a, n):
    inc = a[0]
    exc = 0
    for i in range(1,n):
        temp = inc
        inc = max(inc, exc + a[i])
        exc = temp
    return max(inc,exc)

a = [5, 5, 10, 100, 10, 5]
n = len(a)
print max_sum_sub_nonadj(a,n)
'''
Time Complexity: O(n)
'''
    