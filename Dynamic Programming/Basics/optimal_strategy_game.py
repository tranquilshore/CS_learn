#a = [3,9,1,2]
#a = [8, 15, 3, 7]
#a = [2, 2, 2, 2]
a = [20, 30, 2, 2, 2, 10]
n = len(a)

d = [[(0,0)]*(n) for i in range(n)]

for i in range(n):
    d[i][i] = (a[i],0)

#traversing the upper triangle
for i in range(n):
    for j in range(i+1,n):
        if a[i] + d[i+1][j][1] >= a[j] + d[i][j-1][1]:
            mval = list(d[i][j])
            mval[0] = d[i+1][j][1] + a[i]
            mval[1] = d[i+1][j][0]
            d[i][j] = tuple(mval)
        else:
            mval1 = list(d[i][j])
            mval1[0] = d[i][j-1][1] + a[j]
            mval1[1] = d[i][j-1][0]
            d[i][j] = tuple(mval1)
print d
