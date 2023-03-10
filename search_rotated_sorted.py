# time - O(log n) space - O(1)
def search(nums: list[int], target: int)-> int:
    
    # using binary search
    left, right = 0, len(nums)-1

    # the array has two sorted parts - a left sorted part and a right sorted part
    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        
        # nums[mid] lies in left sorted portion
        if nums[left] <= nums[mid]:
            if target > nums[mid] or target < nums[left]:
                left = mid + 1
            # elif target < nums[left]:     # condensed into single if statement above
            #     left = mid + 1
            else:
                right = mid - 1

        # nums[mid] lies in right sorted portion
        else:
            if target < nums[mid] or target > nums[right]:
                right = mid -1
            # elif target > nums[right]:        # condensed into above if statement
            #     right = mid - 1
            else:
                left = mid + 1
            

    return -1


def main():
    print(search([4,5,6,7,0,1,2], 0))
    print(search([4,5,6,7,0,1,2], 3))
    print(search([1], 0))


main()