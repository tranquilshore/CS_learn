def grid_print(s):
    for i in range(9):
        for j in range(9):
            print s[i][j],
        print "\n"

def find_empty_location(s,l):
    for row in range(9):
        for col in range(9):
            if s[row][col] == 0:
                l[0] = row
                l[1] = col
                return True
    return False

def used_in_row(s,row,num):
    for i in range(9):
        if s[row][i] == num:
            return True
    return False

def used_in_col(s,col,num):
    for i in range(9):
        if s[i][col] == num:
            return True
    return False

def used_in_box(s,row,col,num):
    for i in range(3):
        for j in range(3):
            if s[row+i][col+j] == num:
                return True
    return False

def check_location_is_safe(s,row,col,num):
    return not used_in_row(s,row,num) and not used_in_col(s,col,num) and not used_in_box(s,row - row%3,col - col%3,num)

#backtracking algorithm
def solve_sudoku(s):
    l = [0,0]
    if not find_empty_location(s,l):
        return True
    row = l[0]
    col = l[1]

    for num in range(1,10):
        #if looks promising
        if check_location_is_safe(s,row,col,num):
            #make tentative assignment
            s[row][col] = num
            #return if success
            if solve_sudoku(s):
                return True
            #failure, unmake and try again
            s[row][col] = 0
    #triggers backtracking
    return False

grid=[  [3,0,6,5,0,8,4,0,0],
        [5,2,0,0,0,0,0,0,0],
        [0,8,7,0,0,0,0,3,1],
        [0,0,3,0,1,0,0,8,0],
        [9,0,0,8,6,3,0,0,5],
        [0,5,0,0,9,0,6,0,0],
        [1,3,0,0,0,0,2,5,0],
        [0,0,0,0,0,0,0,7,4],
        [0,0,5,2,0,6,3,0,0] ]

if solve_sudoku(grid):
    grid_print(grid)
else:
    print "No Solution exists" 
            
