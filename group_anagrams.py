from collections import defaultdict
# time - O(m.n.26) = O(m.n) space - O(m) where m is the length of strs and n is the length of the longest string in strs
def group_anagrams(strs: list[str]) -> list[list[str]]:

    # values are defaulted to lists - important to import collections module
    res = defaultdict(list)

    # map the character count sequence to all the strings that have that sequence
    # ex: [111] can map to both "abc" and "cab"
    for s in strs:

        # count will be used as a key in the res map
        count = [0] * 26
        for c in s:
            # using ascii value of char to find index in count list
            count[ord(c) - ord("a")] += 1
        
        # list converted to tuple - only immutable data structures can be used as keys
        # lists are mutable, tuples are not
        res[tuple(count)].append(s)

    return res.values()


def main():
    print(group_anagrams(["eat","tea","tan","ate","nat","bat"]))
    print(group_anagrams([""]))
    print(group_anagrams(["a"]))



main()