# time - O(n^2) space - O(n)
def missing_number_brute(nums: list[int]) -> int:
    # using hashing
    # space - O(n) for extra set
    num_set = set(range(len(nums)+ 1))

    for n in nums:      # O(n)
        num_set.remove(n)   # O(n)
    return num_set

# XOR - nums = [0, 1, 3], n = 3, i = 0, 1, 2, 3
# time - O(n) space - O(1)
def missing_number(nums: list[int]) -> int:
    res = 0
    for i in range(1, len(nums)+1):
        res = res ^ i ^ nums[i-1]

    return res


# sum - take sum of all indices from 0 to n and subtract sum of all elements in nums
# time - O(n) space - O(1)
def missing_number2(nums: list[int]) -> int:
    # sum = 0
    # for i in range(len(nums)+1):
    #     sum += i
    # for n in nums:
    #     sum -= n

    sum = len(nums)
    for i in range(len(nums)):
        sum += (i - nums[i])
    return sum
    

def main():
    print(missing_number_brute([1, 2, 3]))
    print(missing_number([2, 0, 3]))
    print(missing_number2([2, 0, 3]))

main()