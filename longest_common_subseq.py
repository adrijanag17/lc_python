# time - O(mn) space - O(mn)
def length_of_lcs(text1: str, text2: str) -> int:
    # abcde & ace

    m, n = len(text1), len(text2)
    lcs = [[0] * (n+1) for j in range(m + 1)]       # [[column] row]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if text1[i-1] == text2[j-1]:
                lcs[i][j] = 1 + lcs[i-1][j-1]
            else:
                lcs[i][j] = max(lcs[i-1][j], lcs[i][j-1])
    return lcs[m][n]
            

def main():
    text1 = "abcde"
    text2 = "abc"
    print(length_of_lcs(text1, text2))
    print(length_of_lcs("abc", "abc"))
    print(length_of_lcs("abc", "def"))


main()