def binomial(n,k):
    c = [0 for i in xrange(k+1)]
    c[0] = 1
    
    for i in range(1, n+1):
        j = min(i,k)
        while j>0:
            c[j] += c[j-1]
            j -= 1
    return c[k]

n = 5
k = 2
print binomial(n,k)