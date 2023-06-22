class Trie:

    def __init__(self):
        self.root = {}

    # time - O(n) space - O(26.n)
    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur:
                cur[c] = {}
            cur = cur[c]
        cur['*'] = ''


    # time - O(n) space - O(26.n)
    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            if c not in cur:
                return False
            cur = cur[c]
        return '*' in cur


    # time - O(n) space - O(26.n)
    def startWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            if c not in cur:
                return False
            cur = cur[c]
        return True

# alternatively
class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

class Trie2:

    def __init__(self):
        self.root = TrieNode()
    
    
    # time - O(n) space - O(26.n)
    ef insert(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isWord = True
    
    
    # time - O(n) space - O(26.n)
    def search(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.isWord

    
    # time - O(n) space - O(26.n)
    def startsWith(self, prefix):
        cur = self.root
        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True