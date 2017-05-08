def lcs(x,y,m,n):
    L = [[None]*(n+1) for i in xrange(m+1)]
    for i in xrange(m+1):
        for j in xrange(n+1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif x[i-1] == y[j-1]:
                L[i][j] = L[i-1][j-1] + 1
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])
                
    index = L[m][n]
    #creating character array to store the string
    lcs = [""]*(index+1)
    lcs[index] = "\0"
    
    i = m
    j = n
    while i>0 and j>0:
        if x[i-1] == y[j-1]:
            lcs[index-1] = x[i-1]
            i -= 1
            j -= 1
            index -= 1
        #go in the direction of larger value
        elif L[i-1][j] > L[i][j-1]:
            i -= 1
        else:
            j -= 1
            
    print lcs
    
x = "AGGTAB"
y = "GXTXAYB"

m = len(x)
n = len(y)

lcs(x,y,m,n)