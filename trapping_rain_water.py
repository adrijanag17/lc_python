# time - O(n) space - O(1)
def trap(height: list[int]) -> int:

    l, r = 0, len(height) - 1
    lmax, rmax = height[l], height[r]
    res = 0

    while l < r:
        if lmax <= rmax:
            l += 1
            lmax = max(lmax, height[l])
            res += (lmax - height[l])
        else:
            r -= 1
            rmax = max(rmax, height[r])
            res += (rmax - height[r])
    return res


def main():
    print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))
    print(trap([4,2,0,3,2,5]))

main()

