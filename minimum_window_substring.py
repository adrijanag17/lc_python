# time - O(m+n) space - O(m+n)
def min_window(s: str, t: str) -> str:
    countT, window = {}, {}

    for c in t:
        countT[c] = 1 + countT.get(c, 0)

    have, need = 0, len(countT)
    l = 0
    res = [-1, -1]
    res_len = float("infinity")

    for r in range(len(s)):
        c = s[r]
        window[c] = 1 + window.get(c, 0)

        if c in countT and window[c] == countT[c]:
            have += 1

        while have == need:
            if (r - l + 1) < res_len:
                res = [l, r]
                res_len = r - l + 1
            
            # pop characters from the left of string s
            window[s[l]] -= 1
            if s[l] in countT and window[s[l]] < countT[s[l]]:
                have -= 1
            l += 1

    l, r = res
    return s[l:r+1] if res_len != float("infinity") else ""


def main():
    print(min_window("ADOBECODEBANC", "ABC"))
    print(min_window("a", "a"))
    print(min_window("a", "aa"))


main()