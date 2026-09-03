class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l1 = [0] * 26
        for c in s1:
            l1[ord(c) - ord('a')] += 1
        s = 0
        e = len(s1)
        while e <= len(s2):
            l2 = [0] * 26
            for c in s2[s:e]:
                if l1[ord(c) - ord('a')] == 0:
                    break
                l2[ord(c) - ord('a')] += 1
            if l1 == l2:
                return True
            e += 1
            s += 1
        return False