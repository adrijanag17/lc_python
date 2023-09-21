# time - O(2^n) space - O(t * 2^n)
def combinationSum2(candidates: list[int], target: int) -> list[list[int]]:
    candidates.sort()
    res = []

    def dfs(cur, i, total):
        if total == target:
            res.append(cur[:])
            return
        if i == len(candidates) or total > target:
            return
        
        # all subsets that include candidates[i]
        cur.append(candidates[i])
        dfs(cur, i + 1, total + candidates[i])
        cur.pop()

        # if a candidate is duplicate - skip it
        while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
            i += 1

        # all subsets that don't include candidates[i]
        dfs(cur, i + 1, total)
    dfs([], 0, 0)
    return res


def main():
    print(combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))
    print(combinationSum2([2, 5, 2, 1, 2], 5))

main()