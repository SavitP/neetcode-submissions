class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        toReturn = []

        def create(sub ,open, close):
            if close == n:
                toReturn.append(sub)
            else:
                if open < n:
                    sub += "("
                    create(sub, open + 1, close)
                    sub = sub[:len(sub) - 1]
                if close < open:
                    sub += ")"
                    create(sub, open, close + 1)
                    sub = sub[:len(sub) - 1]
        
        create("", 0, 0)
        return toReturn