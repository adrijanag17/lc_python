# time - O(nm) space - O(n)     where n = target and m = len(nums)
def combination_sum_4(nums: list[int], target: int) -> int:

    # using a hashmap for caching; 2d array can also be used here
    dp = { 0 : 1}       # set dp[0] = 1 meaning number of ways to sum up to 0 is 1

    for sum in range(1, target+1):
        dp[sum] = 0
        for n in nums:
            # dp[sum] += dp[sum - n]
            # this is not used because sum - n might become negative and there might not be the corresponding key
            # instead use the get method which only returns the value if key is present else returns a default value (here 0)
            dp[sum] += dp.get(sum - n, 0)
    return dp[target]


def main():
    print(combination_sum_4([1, 2, 3], 4))

main()