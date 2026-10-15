class Solution:
    def numDecodings(self, s: str) -> int:
        m = {}
        def explore(curr):
            if (len(curr) == 1 and curr[0] != "0") or curr == "":
                return 1
            if curr[0] == "0":
                return 0
            if curr in m:
                return m[curr]
            if curr[0] == "1" or (curr[0] == "2" and curr[1] != "7" and curr[1] != "8" and curr[1] != "9"):
                num1 = explore(curr[1:])
                num2 = explore(curr[2:])
                m[curr] = num1 + num2
                return num1 + num2
            num = explore(curr[1:])
            m[curr] = num
            return num
        return explore(s)