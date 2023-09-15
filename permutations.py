# time - O(n . n!) space - O(n . n!)
def permutations(nums: list[int]) -> list[list[int]]:
    res = []
    visited = set()

    def dfs(perm):
        if len(perm) == len(nums):
            res.append(perm[:])
            return
        for i in range(len(nums)):
            if nums[i] not in visited:
                visited.add(nums[i])
                perm.append(nums[i])
                dfs(perm)
                perm.pop()
                visited.remove(nums[i])

    dfs([])
    return res


def main():
    print(permutations([1, 2, 3]))
    print(permutations([0, 1]))
    print(permutations([1]))


main()