# time - O(nlogn) space - O(n)
def counting_bits(n: int) -> list[int]:
    res = []

    for i in range(n+1):
        count = 0
        while i:
            count += i & 1
            i = i >> 1
        res.append(count)

    return res

# time - O(n) space - O(n)
def counting_bits2(n: int) -> list[int]:
    dp = [0] * (n+1)
    offset = 1

    for i in range (1, n+1):
        if offset * 2 == i:
            offset = i
        dp[i] = 1 + dp[i - offset]

    return dp
        
        

def main():
    print(counting_bits2(2))
    print(counting_bits2(3))
    print(counting_bits2(5))
    print(counting_bits2(7))

main()