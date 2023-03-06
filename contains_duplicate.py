# time - O(n) space - O(n)
def containsDuplicate(nums: list[int])->bool:
    
    # dictionary to keep count of a num's repetitions
    num_count = {}

    for n in nums:
        if n in num_count:
            return True
        num_count[n] = 1

    return False

# time - O(n) space - O(n)
def containsDuplicate2(nums: list[int]) -> bool:

    # hashset to store the numbers in nums
    hset = set()

    for n in nums:
        if n in hset:
            return True
        hset.add(n)

    return False

def main():
    print(containsDuplicate2([1,2,3,1]))
    print(containsDuplicate2([1,2,3,4]))
    print(containsDuplicate2([1,1,1,3,3,4,3,2,4,2]))

main()
