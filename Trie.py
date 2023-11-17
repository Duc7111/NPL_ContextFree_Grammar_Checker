
class Trie:

    def __init__(self) -> None:
        self.childs = {}
        self.val = None             
    
    def __iadd__(self, word: list, val) -> None:
        if val is None: return
        cur = self
        for char in word:
            if cur.childs[char] is None:
                cur.childs[char] = Trie()
            cur = cur.childs[char]
        cur.val = val

    def search(self, word: list):
        cur = self
        for char in word:
            if cur.childs[char] is None : return None
            cur = cur.childs[char]
        return cur.val
    
    def load(self, dir: str) -> None:
        file = open(dir, 'r')
        dictionary = {}        
        word = file.readline().replace('\n', '')
        while word != '':
            pos = word.split(',')
            w = pos.pop(0) 
            dictionary[w] = pos
            word = file.readline().replace('\n', '')

        for word, val in dictionary.items():
            self.__iadd__(word, val)
