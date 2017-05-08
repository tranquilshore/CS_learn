#XOR 
def missing_number(a,n):
    x1 = a[1]
    for i in range(2,n):
        x1 = x1^a[i]
    x2 = 1
    for i in range(1,n+1):
        x2 = x2^i
    res = x1^x2
    return res
'''
Time complexity : O(n)
'''