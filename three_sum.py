# time - O(n^2) space - O(n) because timsort space complexity is O(n)
def threeSum(nums:list[int])-> list[list[int]]:
    
    # we do not need the indices so we may sort the array
    nums.sort()
    res = []

    for i, a in enumerate(nums):
        
        # if element is same as last element, go to the next element - to avoid duplicates in the result
        if i > 0 and a == nums[i-1]:
            continue

        l, r = i+1, len(nums) - 1
        target = 0 - a

        while l < r:
            if nums[l] + nums[r] == target:
                res.append([a, nums[l], nums[r]])
                l += 1

                # if left pointer lands on element with same value as previous, skip until different element found - to avoid duplicates
                while l < r and nums[l] == nums[l-1]:
                    l +=1
            elif nums[l] + nums[r] < target:
                l += 1
            else:
                r -= 1

    return res
        

def main():

    print(threeSum([-1, 0, 1, 2, -1, -4]))

main()