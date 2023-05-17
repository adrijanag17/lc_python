# time - O(n^2) space - O(n)
def length_of_lis(nums: list[int]) -> int:
    # lis[i] means length of lis starting at i
    # [1, 2, 5, 3] use as example
    lis = [1] * (len(nums))
    for i in range(len(nums) - 1, -1, -1):
        for j in range(i + 1, len(nums)):
            if nums[i] < nums[j]:
                lis[i] = max(lis[i], 1 + lis[j])
                
    return max(lis)


def main():
    print(length_of_lis([10, 9, 2, 5, 3, 7, 101, 18]))
    print(length_of_lis([0,1,0,3,2,3]))
    print(length_of_lis([7,7,7,7,7,7,7]))


main()