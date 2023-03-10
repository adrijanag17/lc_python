# time - O(n) space - O(n)
def twoSumDictionary(nums: list[int], target: int)-> list[int]:

    # nums is already sorted in ascending order
    # nums is 1 indexed
    # question says must use O(1) space - this solution can't be used
    map = {}
    for i in range(len(nums)):
        comp = target - nums[i]
        if comp in map:
            return [map[comp], i+1]
        map[nums[i]] = i + 1

    return []

# time - O(n) space - O(1)
def twoSum(nums: list[int], target: int)-> list[int]:

    # using two pointers because the array is already sorted
    left, right = 0, len(nums) - 1
    while left < right:
        s = nums[left] + nums[right]
        if s == target:
            return [left+1, right+1]

        elif s < target:
            left += 1
        else:
            right -= 1
    return []


def main():
    print(twoSum([2,7,11,15], 9))
    print(twoSum([2,3,4], 6))
    print(twoSum([-1,0], -1))

main()