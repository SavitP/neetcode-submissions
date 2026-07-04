class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        com = s[0:1]
        map = {com : 1}
        max = 1
        l = 0
        r = 0
        for i in range(len(s)):
            r += 1
            if s[r:r+1] not in map:
                map[s[r:r+1]] = 0
            map[s[r:r+1]] += 1
            if map[s[r:r+1]] > map[com]:
                com = s[r:r+1]
            if r - l + 1 - map[com] > k:
                while r - l + 1 - map[com] > k:
                    map[s[l:l+1]] -= 1
                    if s[l:l+1] == com:
                        for let in map:
                            if map[let] > map[com]:
                                com = let
                    l += 1
            if r - l + 1 > max:
                max = r - l + 1
        if max > len(s):
            max = len(s)
        return max