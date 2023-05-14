# time - O(1) space - O(1)
def reverse_bits(n : int) -> int:
    if n == 0:
        return 0
    res = 0
    for i in range(32):
        res = res << 1
        res += n & 1
        n = n >> 1
    return res


def main():
    print(reverse_bits(43261596))
    print(reverse_bits(4294967293))


main()