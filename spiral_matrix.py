# time - O(m.n) space - O(1)
def spiral_matrix(matrix: list[list[int]]) -> list[int]:
    left, right = 0, len(matrix[0])
    top, bottom = 0, len(matrix)

    res = []

    while left < right and top < bottom:

        # add all numbers in top row
        for i in range(left, right):
            res.append(matrix[top][i])
        top += 1

        # add all numbers in right col
        for i in range(top, bottom):
            res.append(matrix[i][right - 1])
        right -= 1

        # break out if no more row/col
        if not (left < right and top < bottom):
            break

        # add all numbers in bottom row
        for i in range(right - 1, left - 1, -1):
            res.append(matrix[bottom - 1][i])
        bottom -= 1

        # add all numbers in left row
        for i in range(bottom - 1, top - 1, -1):
            res.append(matrix[i][left])
        left += 1

    return res


def main():

    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    print(spiral_matrix(matrix))

    matrix2 = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    print(spiral_matrix(matrix2))

main()