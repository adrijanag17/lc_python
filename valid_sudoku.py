from collections import defaultdict

# time - O(9^2) space - O(3*(9^2))
def valid_sudoku(board: list[list[int]]) -> bool:

    # three hashmaps - one to map each row to the set of numbers it has;
    # one for each col and one for each 3X3 grid
    row = defaultdict(set)
    col = defaultdict(set)
    grid = defaultdict(set)

    for r in range(9):
        for c in range(9):
            if board[r][c] != ".":
                if (board[r][c] in row[r] or
                    board[r][c] in col[c] or
                    board[r][c] in grid[(r//3, c//3)]):
                    return False
                
                row[r].add(board[r][c])
                col[c].add(board[r][c])
                grid[(r//3, c//3)].add(board[r][c])

    return True
