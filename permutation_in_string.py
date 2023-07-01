# time - O(n) space - O(26 * 2) = O(1) where n = len(s2)

def checkInclusion(s1: str, s2: str) -> bool:
    if len(s1) > len(s2):
        return False
    s1Count, s2Count = [0] * 26, [0] * 26

    for i in range(len(s1)):
        s1Count[ord(s1[i]) - ord('a')] += 1
        s2Count[ord(s2[i]) - ord('a')] += 1
    matches = 0

    for i in range(26):
        if s1Count[i] == s2Count[i]:
            matches += 1
    l = 1
    for r in range(len(s1), len(s2)):
        if matches == 26: return True

        index = ord(s2[r]) - ord('a')
        s2Count[index] += 1
        if s1Count[index] == s2Count[index]:
            matches += 1
        elif s1Count[index] + 1 == s2Count[index]:
            matches -= 1

        index = ord(s2[l-1]) - ord('a')
        s2Count[index] -= 1
        if s1Count[index] == s2Count[index]:
            matches += 1
        elif s1Count[index] - 1 == s2Count[index]:
            matches -= 1

        l += 1

    return matches == 26

        
def main():
    print(checkInclusion("ab", "eidbaooo"))
    print(checkInclusion("ab", "eidboaoo"))
    print(checkInclusion("abc", "xyczcab"))


main()