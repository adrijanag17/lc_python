# time - O() space - O()
def genParentheses(n: int) -> list[str]:
    res = []

    def backtrack(openN, closeN, string):
        if openN == closeN == n:
            res.append(string)
            return
        if openN < n:
            backtrack(openN + 1, closeN, string + "(")
        if closeN < openN:
            backtrack(openN, closeN + 1, string + ")")

    backtrack(0, 0, "")
    return res


def main():
    print(genParentheses(2))
    print(genParentheses(3))
    print(genParentheses(1))


main()