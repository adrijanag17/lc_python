# time - O(n^2 * m) space - O(n) - where len(s) = n and len(wordDict) = m
def word_break(s: str, wordDict: list[str]) -> bool:
    # s = "leetcode" & wordDict = ["leet", "code"]
    dp = [False] * (len(s) + 1)
    dp[len(s)] = True

    # dp[i] = True means everything after dp[i] can be found in wordDict
    for i in range(len(s) - 1, -1, -1):
        for w in wordDict:
            if len(s) - i >= len(w) and s[i:i + len(w)] == w:
                dp[i] = dp[i + len(w)]
            if dp[i]:
                break
    return dp[0]


def main():
     print(word_break("leetcode", ["leet", "code"]))
     print(word_break("leetcode", ["leet", "neet"]))
     print(word_break("catsandog", ["cats", 'cat', 'and', 'dog']))


main()