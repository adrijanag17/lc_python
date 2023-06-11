# time - O(n^2) space - O(1)
def count_substrings(s: str) -> int:
    count = 0

    def expand(l, r):
        count = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            count += 1
            l -= 1
            r += 1
        return count

    for i in range(len(s)):
        # count palindromes of odd length
        count += expand(i, i)
        
        # count palindromes of even length
        count += expand(i, i + 1)

    return count


def main():
    print(count_substrings("abc"))
    print(count_substrings("aaa"))
    print(count_substrings("aaab"))


main()