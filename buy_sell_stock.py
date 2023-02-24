# using Kadane's algorith
def maxProfit(prices: list[int]) -> int:

    max_profit = 0
    curr_max = 0
    for i in range(1, len(prices)):
        curr_max += prices[i] - prices[i-1]
        curr_max = max(0, curr_max)
        max_profit = max(curr_max, max_profit)

    return max_profit

# using two pointers
def maxProfit2(prices: list[int]) -> int:

    left, right = 0, 1
    max_p = 0

    while right < len(prices):
        if prices[left] < prices[right]:
            profit = prices[right] - prices[left]
            max_p = max(max_p, profit)
        else:
            left = right
        right += 1
    return max_p


def main():
    print(maxProfit([7,1,5,3,6,4]))
    print(maxProfit2([7,1,5,3,6,4]))

main()