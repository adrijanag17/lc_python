# time - O(1) space - O(1)
def hamming_weight(num : int) -> int:
    # input is 32 bit integer - unsigned
    count = 0
    while num:
        if (num & 1) == 1:
            count += 1
        num = num >> 1

    # handle negative numbers - ??
    return count

def hamming_weight2(num : int) -> int:
    count = 0
    while num:
        count += num % 2
        num = num >> 1

    return count

# time - O(m) where m is the number of 1 bits in the number
def hamming_weight3(n : int) -> int:
    res = 0
    while n:
        n &= (n-1)
        res += 1

    return res




def main():
    print(hamming_weight(11))
    print(hamming_weight(128))
    # print(hamming_weight(-3))

    print(hamming_weight2(11))
    print(hamming_weight2(128))

    print(hamming_weight3(11))
    print(hamming_weight3(128))
    # print(hamming_weight3(-3))


main()