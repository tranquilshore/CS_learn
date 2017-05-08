import operator

def build_suffix_array(txt, n):
    dct = {}
    for i in range(n):
        dct[i] = txt[i:]
    
    #will give the list of tuples
    suffixes = sorted(dct.items(), key=operator.itemgetter(1))
    
    suffixarr = list()
    for j in range(n):
        suffixarr.append(suffixes[j][0])
        
    return suffixarr

#doing a simple binary search for pat in txt using built suffix array
def search(pat, txt, suffixarr, n):
    m = len(pat)
    l = 0
    r = n-1
    
    while l<=r :
        mid = l + (r-l)/2
        match_str = txt[suffixarr[mid]:]
        if pat == match_str[:m]:
            print "found at", suffixarr[mid]
            
        if pat < match_str[:m]:
            r = mid - 1
        else:
            l = mid + 1
        
txt = "sahil"
pat = "ah"

n = len(txt)
suffixarr = build_suffix_array(txt, n)
search(pat, txt, suffixarr, n)

'''
if suffix array is alredy built the above search will take
O(mlogn) time 


'''