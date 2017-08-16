import sys
def minjumps_dp(a):
    n = len(a)
    jumps = [sys.maxint]*n

    if a[0] == 0 or n == 0:
        return sys.maxint

    jumps[0] = 0

    for i in range(1,n):
        for j in range(0,i):
            if i <= j+a[j] and jumps[j] != sys.maxint:
                jumps[i] = min(jumps[i], jumps[j] + 1)
    return jumps[n-1]

#stairs and ladder concept for linear solution
def minjumps_linear(a):
    if len(a) <= 1:
        return 0
    ladder = a[0]
    stairs = a[0]
    jumps = 1
    for level in range(1,len(a)):
        if level == len(a) - 1:
            return jumps
        if level + a[level] > ladder:
            ladder = level + a[level]
        stairs -= 1
        if stairs == 0:
            jumps += 1
            stairs = ladder - level
    return jumps
a = [2,3,1,1,2,4,2,0,1,1]
print minjumps_linear(a)
