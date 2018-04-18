#efficient sudoku solver
def sudoku(arr):
    if not complete(arr):
        r, c = get_first_empty(arr)
        for temp in range(1,10):
            arr[r][c] = temp
            if validate(arr, r, c, temp):
                sudoku(arr)
                if complete(arr):
                    return arr
            arr[r][c] = 0
    return arr

def complete(arr):
    for row in range(9):
        for col in range(9):
            if arr[row][col] == 0:
                return False
    
    return True

def get_first_empty(arr):
    for row in range(9):
        # print(arr[row])
        for col in range(9):
            if arr[row][col] == 0:
                return row, col
    
    return False


def validate(arr, i, j, val):
    if validaterow(arr, i, val) and validatecolumn(arr, j, val):
        return True
    
    return False

def validaterow(arr, row, value):
    found = False
    r = arr[row]
    for v in r:
        if v == value:
            if found:
                return False
            else:
                found = True
    
    return True

def validatecolumn(arr, column, value):
    found = False
    for row in arr:
        if row[column] == value:

            if found:
                return False
            else:
                found = True
    
    return True

def printArr(arr):
    for row in easy:
        print(row)

easy = [[2,9,0,0,0,0,0,7,0],
       [3,0,6,0,0,8,4,0,0],
       [8,0,0,0,4,0,0,0,2],
       [0,2,0,0,3,1,0,0,7],
       [0,0,0,0,8,0,0,0,0],
       [1,0,0,9,5,0,0,6,0],
       [7,0,0,0,9,0,0,0,1],
       [0,0,1,2,0,0,3,0,6],
       [0,3,0,0,0,0,0,5,9]]



sudoku(easy)
printArr(easy)