# time - O(1) space - O(1)

def getSum(a: int, b: int)-> int:

    # mask needed in python to limit size of integer to 32 bit
    mask = 0xffffffff

    while (b != 0):
        c = (a & b) << 1
        a = (a ^ b) & mask
        b = c & mask

    # if a is negative
    if a > mask // 2:
        return ~(a ^ mask)
    else:
        return a


def main():

    print(getSum(2, 3))
    print(getSum(7, 7))
    print(getSum(-1, -3))
    print(getSum(-1, 3))


main()