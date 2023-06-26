from heapq import heappush, heappop
class MedianFinder:

    def __init__(self):
        # two heaps - small (maxheap) & large(minheap)
        self.small = []
        self.large = []


    # time - O(log n) space - O(n)
    def addNum(self, num: int) -> None:
        # add num to small heap (multiple by -1 because maxheap)
        heappush(self.small, -1 * num)

        # check if num added to small heap > smallest val in large heap
        if (self.small and self.large and
            -1 * self.small[0] > self.large[0]):
            val = -1 * heappop(self.small)
            heappush(self.large, val)

        # check if heap lengths almost equal
        if len(self.small) > len(self.large) + 1:
            val = -1 * heappop(self.small)
            heappush(self.large, val)
        if len(self.large) > len(self.small) + 1:
            val = heappop(self.large)
            heappush(self.small, -1 * val)


    # time - O(1) space - O(1)
    def findMedian(self) -> float:
        # if total no. of elements odd
        if len(self.small) > len(self.large):
            return -1 * self.small[0]

        if len(self.large) > len(self.small):
            return self.large[0]

        # if total no. of elements even
        return (-1 * self.small[0] + self.large[0]) / 2

