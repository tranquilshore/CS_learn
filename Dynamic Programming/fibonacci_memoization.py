lookup = [None]*101

def fib(n, lookup):
    if n == 0 or n == 1:
        lookup[n] = n
    
    if lookup[n] is None:
        lookup[n] = fib(n-1, lookup) + fib(n-2, lookup)
        
    return lookup[n]
