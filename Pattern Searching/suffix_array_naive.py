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

txt = "banana"
n = len(txt)

print build_suffix_array(txt,n)

'''
time complexity: O(n^2logn)
as we are doing sorting by comparison and comparison itself takes O(n)
'''

    