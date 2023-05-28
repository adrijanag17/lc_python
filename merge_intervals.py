# time - O(nlogn) space - O(n)
def merge_intervals(intervals: list[list[int]]) -> list[list[int]]:

    # sort the intervals by start values
    intervals.sort(key = lambda i : i[0])
    
    # result list initialized with first interval - to cover edge case where there is only one interval
    output = [intervals[0]]

    for start, end in intervals[1:]:
        last_end = output[-1][1]
        if start <= last_end:
            output[-1][1] = max(end, last_end)

        else:
            output.append([start, end])

    return output



def main():
    print(merge_intervals([[1,3],[2,6],[8,10],[15,18]]))
    print(merge_intervals([[1,4],[4,5]]))

main()