R = int(input("how many rows: "))
C = int(input("how many columns: "))


M = [[int(i) for i in raw_input().split()] for j in range(R)]

def max_sqr_one(M,R,C):
    S = [ [0 for i in range(C)] for j in range(R)]
    for i in range(R):
        S[i][0] = M[i][0]
    for j in range(C):
        S[0][j] = M[0][j]
    
    for i in range(R):
        for j in range(C):
            if M[i][j] == 1:
                S[i][j] = min(S[i][j-1], S[i-1][j], S[i-1][j-1]) + 1
            else:
                S[i][j] = 0
    max_of_s = S[0][0]
    for i in range(R):
        for j in range(C):
            if max_of_s < S[i][j]:
                max_of_s = S[i][j]
    return max_of_s

print max_sqr_one(M,R,C)
    
            
   
