# time - O(n) space - O(1)
def maxArea(height: list[int])-> int:

    max_area = 0
    l, r = 0, len(height) - 1

    while l < r:
        length = min(height[l], height[r])
        breadth = r - l
        area = length * breadth
        max_area = max(max_area, area)
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1

    return max_area

def main():

    print(maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
    print(maxArea([1, 1]))

main()