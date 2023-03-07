# time - O(n) space - O(1)
def maxSubarray(nums: list[int])-> int:

    # using Kadane's algorithm
    max_sum = nums[0]
    curr_max = nums[0]
    for i in range(1, len(nums)):
        curr_max = max(nums[i], curr_max+nums[i])  # we take the max of current number and sum of current number with previous sum because there are negative numbers
        max_sum = max(max_sum, curr_max)

    return max_sum
    

def main():
    print(maxSubarray([6, 2, -3, 4]))
    print(maxSubarray([-2,1,-3,4,-1,2,1,-5,4]))

main()