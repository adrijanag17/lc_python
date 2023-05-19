# time - O(mn) space - O(mn)
def unique_paths(m: int, n: int) -> int:

    dp = [[0] * n for _ in range(m)]
    dp[0][0] = 1

    for i in range(m):
        for j in range(n):
            if i - 1 >= 0:
                dp[i][j] += dp[i-1][j]

            if j - 1 >= 0:
                dp[i][j] += dp[i][j-1]

    return dp[m-1][n-1]

def main():
    print(unique_paths(2, 3))


main()