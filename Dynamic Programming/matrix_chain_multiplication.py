'''
formula:
T[i][j] = min{T[i][k] + T[k+1][j] + value[i]first* value[k]second*value[j]second}

Time Complexity: O(n^3)
Auxiliary Space: O(n^2)
'''
import sys
def matrix_chain_multiplication(p, n):
    m = [[None]*n for i in range(n)]
    #for storing optimal break points to print parenthesis
    bracket = [[None]*n for i in range(n)] 
    
    for i in range(1,n):
        m[i][i] = 0
        
    for l in range(2,n):
        for i in range(1, n-l+1):
            j = i+l-1
            m[i][j] = sys.maxint
            for k in range(i,j):
                q = m[i][k] + m[k+1][j] + p[i-1]*p[k]*p[j]
                if q < m[i][j]:
                    m[i][j] = q
                    #each entry shows where to split
                    bracket[i][j] = k
                    

    name = "A"
    print_parenthesis(1,n-1,n,bracket,name)
    print m[1][n-1]


def print_parenthesis(i,j,n,bracket,name):
    if i == j:
        name = chr(ord(name) + 1)
        print name
        return
    print "("
    
    print_parenthesis(i,bracket[i][j], n, bracket, name)
    print_parenthesis(bracket[i][j] + 1, j, n, bracket, name)
    print ")"
    

a = [40, 20, 30, 10, 30]
size = len(a)

print matrix_chain_multiplication(a,size)