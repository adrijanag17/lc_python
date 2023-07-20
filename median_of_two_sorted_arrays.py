# time - O((n + m)log(n + m)) space - O(n + m)
def findMedianSortedArrays(nums1: list[int], nums2: list[int]) -> float:
    nums = sorted(nums1 + nums2)
    mid1 = len(nums) // 2
    mid2 = mid1 - 1
    if len(nums) % 2 == 0:
        return (nums[mid1] + nums[mid2]) / 2
    return nums[mid1]


def main():
    print(findMedianSortedArrays([1, 3], [2]))
    print(findMedianSortedArrays([1, 2], [3, 4]))


main()