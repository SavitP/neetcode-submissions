class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        map = {"2":["a","b","c"],
        "3":["d","e","f"],
        "4":["g","h","i"],
        "5":["j","k","l"],
        "6":["m","n","o"],
        "7":["p","q","r","s"],
        "8":["t","u","v"],
        "9":["w","x","y","z"]}

        if digits == "":
            return []
        toReturn = []
        self.curr = ""
        def create(s):
            if s == "":
                toReturn.append(self.curr)
                return
            for l in map[s[:1]]:
                self.curr += l
                create(s[1:])
                self.curr = self.curr[:len(self.curr) - 1]
        
        create(digits)
        return toReturn