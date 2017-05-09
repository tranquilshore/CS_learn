def compare(count_pat, count_txt):
    for i in range(256):
        if count_pat[i] != count_txt[i]:
            return False
    return True

def search(pat, txt):
    m = len(pat)
    n = len(txt)
    count_pat = [0]*256
    count_txt = [0]*256
    
    for i in range(m):
        count_pat[ord(pat[i])] += 1
        count_txt[ord(txt[i])] += 1
        
    for i in range(m,n):
        if compare(count_pat, count_txt):
            print "found at ",(i-m)
        #adding the current character to current window
        count_txt[ord(txt[i])] += 1
        #and removing the first of previous window
        count_txt[ord(txt[i-m])] -= 1
    #to check for last window in text
    if compare(count_pat, count_txt):
        print "found at ", (n-m)
        
        
txt = "BACDGABCDA"
pat = "ABCD"
search(pat, txt)

'''
time complexity O(n)

'''