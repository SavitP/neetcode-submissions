class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        toReturn = []
        def gen(s, o, c):
            if o == n and c == n:
                toReturn.append(s)
                return
            if o < n:
                gen(s + "(", o+1, c)
            if c < n and c < o:
                gen(s + ")", o, c+1)
        gen("",0,0)
        return toReturn