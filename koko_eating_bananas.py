import math

# time - O(n * log m) space - O(1) where n = len(piles) and m = max(piles)
def minEatingSpeed(piles: list[int], h: int) -> int:
    l, r = 1, max(piles)
    res = r

    while l <= r:
        k = (l + r) // 2
        time = 0
        for p in piles:
            time += math.ceil(p / k)
        if time <= h:
            res = min(res, k)
            r = k - 1
        else:
            l = k + 1
    return res


def main():
    print(minEatingSpeed([3,6,7,11], 8))
    print(minEatingSpeed([30,11,23,4,20], 5))
    print(minEatingSpeed([30,11,23,4,20], 6))


main()
