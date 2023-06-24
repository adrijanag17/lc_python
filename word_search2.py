class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isWord = True


class Solution:

    # time - O(mn*4^mn) space - O()
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        trie = Trie()
        root = trie.root

        for w in words:
            trie.insert(w)

        ROWS, COLS = len(board), len(board[0])

        res = []

        def dfs(r, c, node, word):
            if node.isWord:
                res.append(word)
            node.isWord = False     # to avoid duplicates in the res (alternatively, can also use a set to store res instead of a list)
            
            if (r < 0 or r == ROWS or c < 0 or c == COLS or
                board[r][c] not in node.children):
                return
            
            word += board[r][c]
            node = node.children[board[r][c]]
            tmp = board[r][c]

            board[r][c] = '#'

            dfs(r - 1, c, node, word)
            dfs(r + 1, c, node, word)
            dfs(r, c - 1, node, word)
            dfs(r, c + 1, node, word)

            board[r][c] = tmp
            
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")

        return res

        

