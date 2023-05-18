# time - O(n) space - O(n)
def house_robber(nums: list[int]) -> int:
    dp = [0] * (len(nums) + 1)

    for i in range(len(nums) - 1, -1, -1):
        if i + 2 <= len(nums):
            dp[i] = max(nums[i] + dp[i+2], dp[i+1])
        else:
            dp[i] = nums[i]

    return dp[0]


# time - O(n) space - O(1)
def house_robber_better(nums: list[int]) -> int:
    rob1, rob2 = 0, 0
    # [rob1, rob2, nums[i], nums[i+1], nums[i+2], ...]
    for n in nums:
        temp = max(rob1 + n, rob2)
        rob1 = rob2
        rob2 = temp
    return rob2


def main():
    print(house_robber([1, 2, 3, 1]))
    print(house_robber_better([1, 2, 3, 1]))


main()
