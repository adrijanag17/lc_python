# time - O(mn) space - O(mn)
def pacific_atlantic(heights: list[list[int]]) -> list[list[int]]:
    rows, cols = len(heights), len(heights[0])
    pac, atl = set(), set()
    res = []

    def flooded_dfs(r, c, ocean, prev_height):

        if (r < 0 or c < 0 or r >= rows or c >= cols
            or (r, c) in ocean or heights[r][c] < prev_height):
            return
        
        ocean.add((r,c))

        flooded_dfs(r - 1, c, ocean, heights[r][c])
        flooded_dfs(r + 1, c, ocean, heights[r][c])
        flooded_dfs(r, c - 1, ocean, heights[r][c])
        flooded_dfs(r, c + 1, ocean, heights[r][c])

    for c in range(cols):
        flooded_dfs(0, c, pac, heights[0][c])
        flooded_dfs(rows-1, c, atl, heights[rows-1][c])

    for r in range(rows):
        flooded_dfs(r, 0, pac, heights[r][0])
        flooded_dfs(r, cols-1, atl, heights[r][cols-1])

    for r in range(rows):
        for c in range(cols):
            if (r, c) in pac and (r, c) in atl:
                res.append([r, c])

    return res


def main():

    print(pacific_atlantic([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]))
    print(pacific_atlantic([[1]]))


main()