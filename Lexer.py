
class EnglishLexer:
    def __init__(self, dir: str) -> None:
        self.dict = {}
        
    # Build for oxford 3000 only since this dictionary only contains: 
    ## [A-z]*
    ## [A-z]* to
    def tokenize(self, string: str) -> list:
        tokens = string.split(' ')
        for i in range(0, len(tokens)):
            if tokens[i] == 'to':
                comToken = tokens[i - 1] + ' ' + tokens[i]
                if comToken in self.dict:
                    tokens[i - 1] = comToken
                    tokens.pop(i)
        return tokens

    # Lexical checker as well as part of speech tagger
    def getPos(self, tokens: list) -> None | list: # None if any of the givens tokens is out of dictionary
        pos = []
        for token in tokens:
            if token in self.dict:
                pos.append(self.dict[token])
            else:
                return None
        return pos
    
    