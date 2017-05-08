def search(pat, txt):
    m = len(pat)
    n = len(txt)
    for i in range(n-m+1):
        for j in range(m):
            if txt[i+j] != pat[j]:
                break
        if j == m-1:
            print str(i)
        
txt = "AABAACAADAABAAABAA"
pat = "AABA"

search(pat, txt)

'''
O(n) best case
O(m*(n-m+1)) worst case
'''