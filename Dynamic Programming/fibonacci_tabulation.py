def fib(n):
    f = [0]*(n+1)
    f[1] = 1
    f[0] = 1
    for i in xrange(2, n+1):
        f[i] = f[i-1] + f[i-2]
        
    return f[n]
