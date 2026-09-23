class PrefixTree:

    def __init__(self):
        self.s = {}

    def insert(self, word: str) -> None:
        for i in range(len(word)):
            if word[:i] not in self.s:
                self.s[word[:i]] = False
            self.s[word] = True

    def search(self, word: str) -> bool:
        if word in self.s:
            return self.s[word]
        return False

    def startsWith(self, prefix: str) -> bool:
        return prefix in self.s
        