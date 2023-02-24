def twoSum(nums: list[int], target: int) -> list[int]:
    map = {}
        
    for i in range(len(nums)):
        comp = target - nums[i]
        if comp in map:
            return [map[comp], i]
        map[nums[i]] = i

def main():
    indices = twoSum([2,7,11,15], 9)
    print(indices)
    print(twoSum([3,2,4], 6))
    print(twoSum([3,3], 6))

main()

'''
time - O(n)
space - O(n)
'''