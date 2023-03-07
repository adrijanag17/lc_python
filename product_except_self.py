def prodExceptSelf(nums: list[int])->list[int]:
    
    # get the product of all elements of nums and for each index in answer, 
    # divide the product by the element at that index in nums
    # NOT ALLOWED IN QUESTION
    # ALSO WON'T WORK IF ONE OF THE ELEMENTS IS A ZERO - THROWS DIVISION BY ZERO ERROR
    prod = 1
    answer = []
    for n in nums:
        prod *= n
    
    for i in range(len(nums)):
        answer.insert(i, int(prod / nums[i])) 
    
    return answer

# time - O(n) space - O(1)
def productExceptSelf(nums: list[int])-> list[int]:

    answer = [1] * len(nums)
    left, right = 1,1
    
    for i in range(len(nums)):
        answer[i] *= left
        left *= nums[i]

    for i in reversed(range(len(nums))):
        answer[i] *= right
        right *= nums[i]

    return answer


def main():
    print(productExceptSelf([1,2,3,4]))
    print(productExceptSelf([-1,1,0,-3,3]))

main()