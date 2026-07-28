class WordDictionary:

    def __init__(self):
        self.words = set()

    def addWord(self, word: str) -> None:
        self.words.add(word)

    def search(self, word: str) -> bool:
        ogword = word
        if "." not in word:
            return word in self.words
        l = []
        while "." in word:
            i = word.find(".")
            l.append(i)
            word = word[:i] + word[i+1:]
        for entry in self.words:
            if len(ogword) != len(entry):
                continue
            for i in l:
                entry = entry[:i] + entry[i+1:]
            if entry == word:
                return True
        return False
