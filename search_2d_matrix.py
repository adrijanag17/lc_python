# time - O(log(m*n)) space - O(1)
def searchMatrix(matrix: list[list[int]], target: int) -> bool:
    ROWS, COLS = len(matrix), len(matrix[0])
    l, r = 0, (ROWS * COLS) - 1

    while l <= r:
        mid = (l + r) // 2
        num = matrix[mid // COLS][mid % COLS]

        if num == target:
            return True
        elif num < target:
            l = mid + 1
        else:
            r = mid - 1
    return False


def main():
    print(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))
    print(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13))


main()
