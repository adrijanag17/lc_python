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


def main():
    print(top_k_freq([1, 1, 1, 2, 2, 3], 2))
    print(top_k_freq([1], 1))


main()

