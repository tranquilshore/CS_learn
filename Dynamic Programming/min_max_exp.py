import sys
def isoperator(op):
    return op == "+" or op == "*"

def min_max_val_exp(exp):
    tmp = ""
    opr = list()
    num = list()
    #storing operator and number in different list
    for i in range(len(exp)):
        if isoperator(exp[i]):
            opr.append(exp[i])
            num.append(int(tmp))
            tmp = ""
        else:
            tmp += exp[i]
            
    num.append(int(tmp))
    print opr
    print num
    
    n = len(num)
    minval = [[None]*n for i in range(n)]
    maxval = [[None]*n for i in range(n)]
    
    for i in range(n):
        for j in range(n):
            minval[i][j] = sys.maxint
            maxval[i][j] = 0
            
            if i == j:
                minval[i][j] = maxval[i][j] = num[i]
    
    #looping exactly like matrix chain multiplication and updating both arrays
    
    for l in range(2,n+1):
        for i in range(n-l+1):
            j = i+l-1
            for k in range(i,j):
                mintmp = 0
                maxtmp = 0
                if opr[k] == '+':
                    mintmp = minval[i][k] + minval[k+1][j]
                    maxtmp = maxval[i][k] + maxval[k+1][j]
                    
                elif opr[k] == '*':
                    mintmp = minval[i][k]*minval[k+1][j]
                    maxtmp = maxval[i][k]*maxval[k+1][j]
                    
                if mintmp < minval[i][j]:
                    minval[i][j] = mintmp
                if maxtmp > maxval[i][j]:
                    maxval[i][j] = maxtmp
    print "minimum: ", minval[0][n-1], " maximum ", maxval[0][n-1]
    
    
exp = "1+2*3+4*5"
min_max_val_exp(exp)

                    