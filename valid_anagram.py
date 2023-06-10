# time - O(s) space - O(s+t) where s and t are lengths of s and t
def valid_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    
    s_count, t_count = {}, {}
    for i in range(len(s)):
        s_count[s[i]] = 1 + s_count.get(s[i], 0)
        t_count[t[i]] = 1 + t_count.get(t[i], 0)

    for c in s:
        if s_count[c] != t_count.get(c, 0):
            return False

    return True


# time - O(nlogn) space - O(1)
def valid_anagram2(s: str, t: str) -> bool:
    return sorted(s) == sorted(t)


def main():
    print(valid_anagram("anagram", "nagaram"))
    print(valid_anagram2("anagram", "nagaram"))
    print(valid_anagram("rat", "car"))
    print(valid_anagram2("rat", "car"))


main()