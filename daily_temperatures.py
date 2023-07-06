# time - O(2n) = O(n) space - O(n)
def dailyTemp(temp: list[int]) -> list[int]:
    # using monotonic stack
    res = [0] * len(temp)
    stack = []
    for i, t in enumerate(temp):
        while stack and temp[stack[-1]] < t:
            cur = stack.pop()
            res[cur] = i - cur
        stack.append(i)
    return res


def main():
    print(dailyTemp([73,74,75,71,69,72,76,73]))
    print(dailyTemp([30,40,50,60]))
    print(dailyTemp([30,60,90]))


main()