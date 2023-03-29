# time - O(1) space - O(1)

def getSum(a: int, b: int)-> int:
    while (b != 0):
        c = (a & b) << 1
        a = a ^ b
        b = c

    return a


def main():

    print(getSum(2, 3))
    print(getSum(7, 7))


main()