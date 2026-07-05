class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        s1l = [0] * 26
        for s in s1:
            s1l[ord(s) - ord('a')] += 1
        s2l = [0] * 26
        for s in s2[0:len(s1)]:
            s2l[ord(s) - ord('a')] += 1
        if s1l == s2l:
            return True
        l = 0
        r = len(s1) - 1
        while (r < len(s2) - 1):
            print(s2[l:r + 1])
            s2l[ord(s2[l]) - ord('a')] -= 1
            l += 1
            r += 1
            s2l[ord(s2[r]) - ord('a')] += 1
            if s1l == s2l:
                return True
        return False