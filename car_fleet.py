# time - O(nlogn) space - O(n)
def carFleet(target: int, position: list[int], speed: list[int]) -> int:
    fleets = 0
    posSpeedPairs = [[p, s] for p, s in zip(position, speed)]
    prev = None

    for p, s in sorted(posSpeedPairs)[::-1]:
        if not prev or prev < (target - p) / s:
            fleets += 1
            prev = (target - p) / s

    return fleets


# using stack - time - O(nlogn) space - O(n)
def carFleet2(target: int, position: list[int], speed: list[int]) -> int:
    stack = []
    pairs = [[p, s] for p, s in zip(position, speed)]

    for p, s in sorted(pairs)[::-1]:
        stack.append((target - p) / s)
        if len(stack) >= 2 and stack[-2] >= stack[-1]:
            stack.pop()
    return len(stack)


def main():
    print(carFleet2(12, [10,8,0,5,3], [2, 4, 1, 1, 3]))
    print(carFleet2(10, [3], [3]))


main()