
from Trie import Trie

class Lexer:
    def __init__(self, dir: str) -> None:
        self.trie = Trie()
        self.trie.load(dir)

    def tokenize(self, string: str) -> []:
        tokens = []
        cur: Trie
        s = 0
        n = len(string)
        while s < n:
            cur = self.trie
            e = None
            for i in range(s, n):
                if cur.childs[string[i]] is None: 
                    break
                cur = cur.childs[string[i]]
                if cur.val is not None:
                    e = i
            if e is not None:
                tokens.append(str[s:e])
            else 