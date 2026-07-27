class PrefixTree:

    def __init__(self):
        self.map = {}

    def insert(self, word: str) -> None:
        for i in range(1, len(word)):
            if word[:i] not in self.map:
                self.map[word[:i]] = False
        self.map[word] = True

    def search(self, word: str) -> bool:
        return word in self.map and self.map[word]

    def startsWith(self, prefix: str) -> bool:
        return prefix in self.map
        