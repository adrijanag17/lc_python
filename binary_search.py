# time - O(log n) space - O(1)
def search(nums: list[int], target: int) -> int:

    res = -1
    l, r = 0, len(nums) - 1

    while l <= r:
        mid = (l + r) // 2
        if nums[mid] < target:
            l = mid + 1
        elif nums[mid] > target:
            r = mid - 1
        else:
            res = mid
            break

    return res


def main():
    print(search([-1,0,3,5,9,12], 9))
    print(search([-1,0,3,5,9,12], 2))


main()