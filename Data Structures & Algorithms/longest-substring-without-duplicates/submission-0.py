class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        letters = set()
        l = 0
        longest = 0
        for i in range(len(s)):
            if s[i:i+1] in letters:
                while s[l:l+1] != s[i:i+1]:
                    letters.remove(s[l:l+1])
                    l += 1
                l += 1
            else:
                letters.add(s[i:i+1])
            if i - l + 1 > longest:
                longest = i - l + 1
        return longest
        