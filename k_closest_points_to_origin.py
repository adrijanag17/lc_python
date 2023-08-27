import heapq
import math

# time - O(n log n) space - O(n)
def kClosest(points: list[list[int]], k: int) -> list[list[int]]:
    minHeap = []
    res = []
    for x, y in points:
        dist = math.sqrt((x ** 2) + (y ** 2))
        heapq.heappush(minHeap, (dist, [x, y]))

    for i in range(k):
        _, point = heapq.heappop(minHeap)
        res.append(point)

    return res


def main():
    print(kClosest([[1,3],[-2,2]], 1))
    print(kClosest([[3,3],[5,-1],[-2,4]], 2))


main()