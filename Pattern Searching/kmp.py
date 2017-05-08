#longest prefix which is also a suffix
def computeLPSarray(pat, m, lps):
    length = 0 
    i = 1
    while i < m:
        if pat[i] == pat[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length-1]
            else:
                lps[i] = 0
                i += 1
                
def KMPsearch(pat, txt):
    m = len(pat)
    n = len(txt)
    
    lps = [0]*m
    j = 0 #index for pattern
    
    computeLPSarray(pat, m, lps)
    
    i=0 #index for text
    while i < n:
        if pat[j] == txt[i]:
            i += 1
            j += 1
            
        if j == m:
            print "found pattern at: ", str(i-j)
            j = lps[j-1]
            
        elif i < n and pat[j] != txt[i]:
            if j != 0:
                j = lps[j-1]
            else:
                i += 1
                
txt = "ABABDABACDABABCABAB"
pat = "ABABCABAB"
KMPsearch(pat, txt)