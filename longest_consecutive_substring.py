# time - O(n) space - O(n)
def longest_consecutive(nums: list[int]) -> int:
    num_set = set(nums)
    max_len = 0

    for n in nums:
        curr_len = 1
        if n - 1 not in num_set:
            m = n + 1
            while m in num_set:
                curr_len += 1
                m += 1
        max_len = max(max_len, curr_len)

    return max_len

def main():
    print(longest_consecutive([100,4,200,1,3,2]))
    print(longest_consecutive([0,3,7,2,5,8,4,6,0,1]))


main()