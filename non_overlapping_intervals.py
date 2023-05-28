# time - O(nlogn) space - O(1)
def non_overlapping_intervals(intervals: list[list[int]]) -> int:

    count = 0
    intervals.sort(key = lambda i : i[0])
    prev_end = intervals[0][1]

    for start, end in intervals[1:]:
        if start >= prev_end:
            prev_end = end

        else:
            count += 1
            prev_end = min(prev_end, end)

    return count


def main():
    print(non_overlapping_intervals([[1,2],[2,3],[3,4],[1,3]]))
    print(non_overlapping_intervals([[1,2],[1,2],[1,2]]))
    print(non_overlapping_intervals([[1,2],[2,3]]))

main()