# time - O(mn) space - O(1)
def set_zeroes(matrix: list[list[int]]) -> None:
    ROWS, COLS = len(matrix), len(matrix[0])

    # for tracking row 0
    row_zero = False

    # marking rows and cols to be set to 0
    for r in range(ROWS):
        for c in range(COLS):
            if matrix[r][c] == 0:
                matrix[0][c] = 0
                if r > 0:
                    matrix[r][0] = 0
                else:
                    row_zero = True

    # setting rows and cols to zero
    for r in range(1, ROWS):
        for c in range(1, COLS):
            if matrix[0][c] == 0 or matrix[r][0] == 0:
                matrix[r][c] = 0

    if matrix[0][0] == 0:
        for r in range(ROWS):
            matrix[r][0] = 0
        

    if row_zero:
        for c in range(COLS):
            matrix[0][c] = 0
            

def main():

    test1 = [[1,1,1],[1,0,1],[1,1,1]]
    set_zeroes(test1)
    print(test1)

    test2 = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    set_zeroes(test2)
    print(test2)



main()