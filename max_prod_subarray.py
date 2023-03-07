# time - O(n) space - O(1)
def maxProdSubarray(nums: list[int])-> int:

    # using Kadane's algorithm - but with max and min both
    curr_max, curr_min = 1, 1
    max_prod = nums[0]

    for n in nums:
        x = max(curr_max * n, curr_min * n, n)
        y = min(curr_max * n, curr_min * n, n)

        curr_max, curr_min = x, y   # x and y used to temporarily store max and min so that while calculating min we do not use the updated value of max

        max_prod = max(max_prod, curr_max)

    return max_prod

def main():
    print(maxProdSubarray([2,3,-2,4]))
    print(maxProdSubarray([2, 3, -2, -2]))
    print(maxProdSubarray([-2,0,-1]))


main()