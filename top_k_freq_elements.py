from heapq import heapify, heappush, heappop

# time - O(nlogk) space - O(m + k) = O(n + k) worst case; where m = # unique nos. in nums
def top_k_freq(nums: list[int], k: int) -> list[int]:

    # map each number to its frequency
    freq = {}
    for n in nums:
        freq[n] = freq.get(n, 0) + 1

    heap = []
    heapify(heap)

    for key, val in freq.items():
        heappush(heap, (val, key))
        if len(heap) > k:
            heappop(heap)

    res = []
    while heap:
        _, key = heap.pop()
        res.append(key)

    return res


# time - O(n) space - O(n)
def top_k_bucket(nums: list[int], k: int) -> list[int]:
    freq = {}

    for n in nums:
        freq[n] = freq.get(n, 0) + 1

    buckets = [[] for _ in range(len(nums) + 1)]

    for key, val in freq.items():
        buckets[val].append(key)

    res = []

    for i in range(len(buckets) - 1, 0, -1):
        for n in buckets[i]:
            res.append(n)
            if len(res) == k:
                return res


def main():
    print(top_k_bucket([1, 1, 1, 2, 2, 3], 2))
    print(top_k_bucket([1], 1))


main()

