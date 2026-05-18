class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters = list(s)
        for letter in t:
            if letter not in letters:
                return False
            letters.remove(letter);
        if (len(letters) > 0):
            return False
        return True