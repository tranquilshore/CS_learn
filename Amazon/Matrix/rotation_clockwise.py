'''
The approach is similar to printing a matrix in spiral form.
Let's discuss that first

k,l----->n
|
|
m

k,l = 0,0
m,n = Row, Col

while k<m and l<n:
    i   l -> n:
        a[k][i]
    k += 1

    i   k -> m:
        a[i][n-1]
    n -= 1

    i   n-1 -> l:
        a[m-1][i]
    m -= 1

    i   m-1 -> k:
        a[l][i]
    l += 1

Now, easy to understand rotation:

top,left------>right
|
|
|
bottom

top,left = 0,0
bottom = len(mat) - 1
right = len(mat[0]) - 1

while left < right and top < bottom:
    #trick here is to store first element of next row which will
    replace first element of current row

    prev = mat[top+1][left]

    #moving top row elements one step right
    i   left -> right + 1:
        curr = mat[top][i]
        mat[top][i],prev = prev, curr
    top += 1

    #moving rightmost col to one step downwards
    i   top -> bottom+1:
        curr = mat[i][right]
        mat[i][right], prev = prev, curr
    right -= 1

    #moving bottom row one step left
    i   right -> left-1:
        curr = mat[bottom][i]
        mat[bottom][i], prev = prev, curr
    bottom -= 1

    #moving leftmost col one step upwards
    i   bottom -> top-1:
        curr = mat[i][left]
        mat[i][left], prev = prev, curr
    left += 1
'''

def rotateMatrix(mat):
 
    if not len(mat):
        return
 
    top = 0
    bottom = len(mat)-1
 
    left = 0
    right = len(mat[0])-1
 
    while left < right and top < bottom:
 
        # Store the first element of next row,
        # this element will replace first element of
        # current row
        prev = mat[top+1][left]
 
        # Move elements of top row one step right
        for i in range(left, right+1):
            curr = mat[top][i]
            mat[top][i] = prev
            prev = curr
 
        top += 1
 
        # Move elements of rightmost column one step downwards
        for i in range(top, bottom+1):
            curr = mat[i][right]
            mat[i][right] = prev
            prev = curr
 
        right -= 1
 
        # Move elements of bottom row one step left
        for i in range(right, left-1, -1):
            curr = mat[bottom][i]
            mat[bottom][i] = prev
            prev = curr
 
        bottom -= 1
 
        # Move elements of leftmost column one step upwards
        for i in range(bottom, top-1, -1):
            curr = mat[i][left]
            mat[i][left] = prev
            prev = curr
 
        left += 1
 
    return mat

def printMatrix(mat):
    for row in mat:
        print row
 
 
# Test case 1
matrix =[ 
            [1,  2,  3,  4 ],
            [5,  6,  7,  8 ],
            [9,  10, 11, 12 ],
            [13, 14, 15, 16 ]  
        ]
# Test case 2
"""
matrix =[
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
"""
 
matrix = rotateMatrix(matrix)
# Print modified matrix
printMatrix(matrix)