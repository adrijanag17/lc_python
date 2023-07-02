import collections

# time - O(n) space - O(n)
def maxSlidingWindow(nums: list[int], k: int) -> list[int]:

    res = []

    # use a monotonically decreasing deque to store indices
    q = collections.deque()
    l = 0

    for r in range(len(nums)):
        while q and nums[q[-1]] < nums[r]:
            q.pop()

        q.append(r)

        if l > q[0]:
            q.popleft()

        if (r + 1) >= k:
            res.append(nums[q[0]])
            l += 1
    return res


def main():
    print(maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))


main()
        


