import heapq

# time - O(k log n) space - O(n)
def findKthLargest(nums: list[int], k: int) -> int:
    maxHeap = [-n for n in nums]
    heapq.heapify(maxHeap)
    for i in range(k - 1):
        heapq.heappop(maxHeap)
    return heapq.heappop(maxHeap) * -1


def main():
    print(findKthLargest([3,2,1,5,6,4], 2))
    print(findKthLargest([3,2,3,1,2,4,5,5,6], 4))


main()