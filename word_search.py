# time - O(m.n.4^(s)) space - O(s) size of stack; where s = len(word)
def word_search(board: list[list[int]], word: str) -> bool:
    ROWS, COLS = len(board), len(board[0])
    path = set()

    def match_dfs(r, c, i):
        if i == len(word):
            return True

        if (r < 0 or r >= ROWS or c < 0 or c >= COLS or 
        board[r][c] != word[i] or (r, c) in path):
            return False

        path.add((r, c))

        res = (match_dfs(r + 1, c, i+1) or
                match_dfs(r - 1, c, i+1) or
                match_dfs(r, c + 1, i+1) or
                match_dfs(r, c - 1, i+1))

        return res

    for r in range(ROWS):
        for c in range(COLS):
            if match_dfs(r, c, 0):
                return True

    return False


def main():
    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word = "ABCCED"
    print(word_search(board, word))

    board2 = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word2 = "SEE"
    print(word_search(board2, word2))

    board3 = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word3 = "ABCB"
    print(word_search(board3, word3))


main()