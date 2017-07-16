def msbpos(n):
    pos = 0
    while n != 0:
        pos += 1
        n = n >> 1
    return pos

def josephify(n):
    position = msbpos(n)
    j = 1 << (position - 1)
    
    #xor operation
    n = n^j
    
    #left shift operation
    n = n << 1
    
    #or operation
    n = n | 1
    
    return n

print josephify(41)