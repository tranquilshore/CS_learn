'''
Cn+1 = E(i=0,n)CiCn-i
T(n) = Sum(T(i)T(n-i-1))
T(n) = 2n!/(n+1)!n!

unlabeled binary trees = catalan number
labeled binary trees = [catalan number] * n!

'''

def catalandp(n):
    catalan = [0]*(n+1)
    catalan[0] = 1
    catalan[1] = 1
    
    for i in range(2,n+1):
        catalan[i] = 0
        for j in range(i):
            catalan[i] += catalan[j] * catalan[i-j-1]
            
    return catalan[n]
print catalandp(3)
    