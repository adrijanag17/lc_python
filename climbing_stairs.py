# recursion
# time - O(2^n) space - O(1)
def climbing_stairs_rec(n: int) -> int:
    if n <= 1:
        return 1
    res = climbing_stairs(n-1) + climbing_stairs(n-2)
    return res

# dp
# time - O(n) space - O(n)
def climbing_stairs(n: int) -> int:
    dp = [0] * (n+1)
    dp[0] = 1
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]
        


def main():
    print(climbing_stairs(3))
    print(climbing_stairs(4))
    print(climbing_stairs(5))
    print(climbing_stairs(6))
    print(climbing_stairs(7))

main()