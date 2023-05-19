# time - O(mn) space - O(n) where n = len(nums) and m = max(nums)
# using dynamic programming
def can_jump(nums: list[int]) -> bool:
    dp = [False] * len(nums)
    dp[-1] = True

    for i in range(len(nums) - 2, -1, -1):
        for j in range(1, nums[i] + 1):
            if dp[i] == True:
                break
            dp[i] = dp[i + j]
    return dp[0]


# time - O(n) space - O(1)
def can_jump_greedy(nums: list[int]) -> bool:
    last_reachable = len(nums) - 1
    for i in range(len(nums) - 2, -1, -1):
        if nums[i] >= last_reachable - i:
            last_reachable = i

    return True if last_reachable == 0 else False

def main():
    print(can_jump_greedy([3, 2, 1, 0, 4]))
    print(can_jump_greedy([2, 3, 1, 1, 4]))


main()