'''
formula for calculating hash:

1. x = old hash - val(old char)
2. x = x/prime
3. new hash = x + prime^(m-1) * val(new char)

'''

# number of characters in input alphabet
d = 256
#q is a prime number
def search(pat, txt, q):
    m = len(pat)
    n = len(txt)
    i = 0
    j = 0
    p = 0 #hash value for pattern
    t = 0 #hash value for text
    h = 1
    
    for i in range(m-1):
        h = (h*d)%q
        
    #calculating hash value of pattern and first window
    for i in range(m):
        p = (d*p + ord(pat[i]))%q
        t = (d*t + ord(txt[i]))%q
        
    for i in range(n-m+1):
        if p == t:
            for j in range(m):
                txt[i+j] != pat[j]:
                    break
            j+= 1
            if j == m:
                print "found at: " + str(i)
                
        if i < n-m:
            t = (d*(t-ord(txt[i])*h) + ord(txt[i+m]))%q
            if t < 0:
                t = t + q
                
                
'''
time complexity:
O(m+n)

'''