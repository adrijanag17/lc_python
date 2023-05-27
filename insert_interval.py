# time - O(n) space - O(n)
def insert_interval(intervals: list[list[int]], new_interval: list[int]) -> list[list[int]]:
    res = []

    for i in range(len(intervals)):
        if new_interval[1] < intervals[i][0]:
            res.append(new_interval)
            res = res + intervals[i:]
            return res
        elif new_interval[0] > intervals[i][1]:
            res.append(intervals[i])

        else:
            new_interval = [min(new_interval[0], intervals[i][0]), max(new_interval[1], intervals[i][1])]

    res.append(new_interval)
    return res

def main():
    print(insert_interval([[1,3],[6,9]], [2,5]))
    print(insert_interval([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]))


main()