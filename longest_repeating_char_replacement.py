# time - O(26.n) = O(n) space - O(m), m is the number of unique letters in the string
def char_replacement(s: str, k: int) -> int:
    char_freq = {}
    res = 0
    left = 0

    for right in range(len(s)):
        char_freq[s[right]] = 1 + char_freq.get(s[right], 0)
        if (right - left + 1) - (max(char_freq.values())) > k:
            char_freq[s[left]] -= 1
            left += 1
        res = max(res, right - left + 1)

    return res
        

def main():
    print(char_replacement("ABAB", 2))
    print(char_replacement("AABABBA", 1))


main()