# time - O(amount * len(coin)) space - O(amount)
def coin_change(coins: list[int], amount: int) -> int:
    dp = [amount + 1] * (amount+1)
    dp[0] = 0
    for a in range(1, amount+1):
        for c in coins:
            if c <= a:
                dp[a] = min(dp[a], 1 + dp[a - c])

    return dp[amount] if dp[amount] != amount + 1 else -1

def main():
    print(coin_change([1, 2, 5], 11))
    print(coin_change([1, 3, 4, 5], 7))


main()