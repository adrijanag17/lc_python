import collections

class TimeMap:

    def __init__(self):
        self.map = collections.defaultdict(list)


    # time - O(1) space - O(m.n) where n = no. of timestamps, m = no. of keys
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append((timestamp, value))


    # time - O(log n) space - O(m.n)
    def get(self, key: str, timestamp: int) -> str:
        valList = self.map[key]
        l, r = 0, len(valList) - 1
        res = ""

        while l <= r:
            mid = (l + r) // 2
            if valList[mid][0] <= timestamp:
                res = valList[mid][1]
                l = mid + 1
            else:
                r = mid - 1
        return res


        
