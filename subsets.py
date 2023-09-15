# time - O(2^n) space - O(n * 2^n)

def subsets(nums: list[list[int]]) -> list[list[int]]:

    res = []

    def dfs(i, subset):

        if i == len(nums):
            res.append(subset[:])
            return
        
        # don't take nums[i]
        dfs(i + 1, subset)

        # take nums[i]
        subset.append(nums[i])
        dfs(i + 1, subset)
        subset.pop()

    dfs(0, [])
    return res


def main():

    print(subsets([1, 2, 3]))


main()