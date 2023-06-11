# time - O(n^2) space - O(1)
def longest_palindromic_substring(s: str) -> str:
    res = [-1, -1]
    res_len = 0

    def expand(l ,r, res_len, res):
        while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > res_len:
                    res = [l, r]
                    res_len = r - l + 1
                l -= 1
                r += 1
        return res, res_len

    for i in range(len(s)):
        # for odd lengths
        l, r = i, i
        res, res_len = expand(l, r, res_len, res)
        
        # for even lengths
        l, r = i, i + 1
        res, res_len = expand(l, r, res_len, res)

    l, r = res
    return s[l:r+1]


def main():
    print(longest_palindromic_substring("babad"))
    print(longest_palindromic_substring("cbbd"))


main()


