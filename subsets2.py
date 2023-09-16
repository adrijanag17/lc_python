# time - O(2^n) space - O(n . 2^n)
def subsetsWithDup(nums: list[int]) -> list[list[int]]:
    res = []

    def dfs(subset, i):
        if i == len(nums):
            res.append(subset[:])
            return

        # add nums[i] to subset
        subset.append(nums[i])
        dfs(subset, i + 1)
        subset.pop()

        # if duplicate - skip
        while i + 1 < len(nums) and nums[i] == nums[i + 1]:
            i += 1

        dfs(subset, i + 1)

    dfs([], 0)
    return res


def main():
    print(subsetsWithDup([1, 2, 2]))
    print(subsetsWithDup([0]))


main()