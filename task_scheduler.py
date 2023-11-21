import heapq
from collections import Counter, deque

# time - O(n) space - O(26) = O(1)
def leastInterval(tasks: list[str], n: int) -> int:
    count = Counter(tasks)
    maxHeap = [-cnt for cnt in count.values()]
    heapq.heapify(maxHeap)
    time = 0
    q = deque()

    while maxHeap or q:
        time += 1
        if maxHeap:
            cur = heapq.heappop(maxHeap) + 1
            if cur:
                q.append([cur, time + n])
        if q and q[0][1] == time:
            heapq.heappush(maxHeap, q.popleft()[0])
    return time

        

def main():
    print(leastInterval(["A","A","A","B","B","B"], 2))
    print(leastInterval(["A","A","A","B","B","B"], 0))
    print(leastInterval(["A","A","A","A","A","A","B","C","D","E","F","G"], 2))



main()