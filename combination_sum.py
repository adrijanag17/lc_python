# time - O(2^t) space - O(t * 2^t)      where t = len(target)

def combinationSum(candidates: list[int], target: int) -> list[list[int]]:
    res = []

    def dfs(i, comb, total):
        if total == target:
            res.append(comb[:])
            return

        if i == len(candidates) or total > target:
            return

        # pick the current index element
        # index remains i because we are allowed to repeat numbers
        comb.append(candidates[i])
        dfs(i, comb, total + candidates[i])
        comb.pop()      # clean up

        # don't pick current index element
        dfs(i + 1, comb, total)

    dfs(0, [], 0)
    return res


def main():

    print(combinationSum([2, 3, 6, 7], 7))
    print(combinationSum([2, 3, 5], 8))
    print(combinationSum([2], 1))


main()