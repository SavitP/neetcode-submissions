class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l1 = [0] * 26
        l2 = [0] * 26
        if len(s2) < len(s1):
            return False
        count = 0
        for c in s1:
            l1[ord(c) - ord('a')] += 1
            l2[ord(s2[count]) - ord('a')] += 1
            count += 1
        if l1 == l2:
                return True
        s = 1
        e = len(s1) + 1
        
        while e <= len(s2):
            l2[ord(s2[e - 1]) - ord('a')] += 1
            l2[ord(s2[s - 1]) - ord('a')] -= 1
            if l1 == l2:
                return True
            e += 1
            s += 1
        return False
