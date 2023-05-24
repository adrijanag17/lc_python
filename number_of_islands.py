# time - O(mn) space - O(mn)
def num_islands(grid: list[list[str]]) -> int:
    rows, cols = len(grid), len(grid[0])
    count = 0

    def erase_island_dfs(r, c):
        if (r < 0 or c < 0 or r >= rows or c >= cols
            or grid[r][c] != "1"):
            return

        grid[r][c] = "0"

        erase_island_dfs(r - 1, c)
        erase_island_dfs(r + 1, c)
        erase_island_dfs(r, c - 1)
        erase_island_dfs(r, c + 1)


    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1":
                erase_island_dfs(r, c)
                count += 1

    return count


def main():

    print(num_islands([
    ["1","1","1","1","0"],
    ["1","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
    ]))

    print(num_islands([
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
    ]))


main()