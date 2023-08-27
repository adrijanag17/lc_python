import heapq
class KthLargest:

    # time - O(nlogn) space - O(k)
    def __init__(self, k: int, nums: list[int]):
        self.minHeap, self.k = nums, k
        heapq.heapify(self.minHeap)     # O(n)
        while len(self.minHeap) > self.k:       # runs n - k times
            heapq.heappop(self.minHeap)     # O(log n) for each pop


    # time - O(logn) space - O(1)
    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)       # O(log n)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)     # O(log n)
        return self.minHeap[0]


def main():
    nums = [5, 8, 1, 6, 2, 0]
    largest = KthLargest(3, nums)
    print(largest.add(1))
    print(largest.add(6))


main()
        
