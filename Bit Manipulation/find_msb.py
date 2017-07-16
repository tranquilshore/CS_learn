def msbpos(n):
    pos = 0
    while n != 0:
        pos += 1
        n = n >> 1 #shifting bits to right
    return pos

print msbpos(n)