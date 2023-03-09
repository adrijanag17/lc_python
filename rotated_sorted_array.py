# time - O(log n) space O(1)
def findMin(nums: list[int])-> int:
    # using binary search
    left, right = 0, len(nums) - 1

    while left < right:

        mid = (left + right) // 2

        if nums[mid] > nums[right]:
            left = mid + 1

        else:
            right = mid

    return nums[left]

def main():
    print(findMin([3,4,5,1,2]))
    print(findMin([4,5,6,7,0,1,2]))

main()