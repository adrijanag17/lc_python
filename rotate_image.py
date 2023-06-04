# time - O(n^2) space - O(1)
def rotate(matrix: list[list[int]]) -> None:
    left, right = 0, len(matrix) - 1
    top, bottom = left, right

    while left < right and top < bottom:

        for i in range(right - left):

            top_left = matrix[top][left + i]
            matrix[top][left + i] = matrix[bottom - i][left]
            matrix[bottom - i][left] = matrix[bottom][right - i]
            matrix[bottom][right - i] = matrix[top + i][right]
            matrix[top + i][right] = top_left

        left += 1
        right -= 1
        top += 1
        bottom -= 1


def main():
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    rotate(matrix)
    print(matrix)

    matrix2 = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    rotate(matrix2)
    print(matrix2)


main()