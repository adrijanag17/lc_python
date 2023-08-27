import heapq

# time - O(n log n) space - O(n)
def stoneWeight(stones: list[int]) -> int:
    maxHeap = []
    for s in stones:
        heapq.heappush(maxHeap, (-1 * s))

    while len(maxHeap) > 1:
        first = heapq.heappop(maxHeap) * -1
        second = heapq.heappop(maxHeap) * -1
        diff = abs(first - second)
        if diff != 0:
            heapq.heappush(maxHeap, diff * -1)

    return 0 if len(maxHeap) == 0 else maxHeap[0] * -1


def main():
    print(stoneWeight([2,7,4,1,8,1]))
    print(stoneWeight([1]))


main()