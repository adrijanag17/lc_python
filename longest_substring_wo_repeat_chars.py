# time - O(n) space - O(n)
def length_of_longest_substring(s: str) -> int:
    char_map = dict()
    l = 0
    res = 0

    for r in range(len(s)):
        if s[r] in char_map:
            l = max(char_map[s[r]] + 1, l)

        char_map[s[r]] = r
        res = max(res, r - l + 1)

    return res


def main():
    print(length_of_longest_substring("abcabcbb"))
    print(length_of_longest_substring("bbbbb"))
    print(length_of_longest_substring("pwwkew"))


main()