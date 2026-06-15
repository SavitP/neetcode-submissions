class Solution:
    def isPalindrome(self, t: str) -> bool:
        s = ""
        for char in t:
            if char.isalnum():
                s+=char.lower()
        return s == s[::-1]
        