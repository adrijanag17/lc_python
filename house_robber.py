# time - O(n) space - O(n)
def house_robber(nums: list[int]) -> int:
    dp = [0] * (len(nums) + 1)

    for i in range(len(nums) - 1, -1, -1):
        if i + 2 <= len(nums):
            dp[i] = max(nums[i] + dp[i+2], dp[i+1])
        else:
            dp[i] = nums[i]

    return dp[0]


def main():
    print(house_robber([1, 2, 3, 1]))


main()
