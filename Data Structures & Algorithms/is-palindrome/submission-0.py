class Solution:
    def isPalindrome(self, t: str) -> bool:
        s = ""
        for char in t:
            if char.isalnum():
                s+=char
        if len(s) % 2 == 0:
            left = (len(s) // 2) - 1
            right = len(s) // 2
        else:
            left = len(s) // 2
            right = len(s) // 2
        while right != len(s):
            if (s[left:left+1].lower() != s[right:right+1].lower()):
                return False
            left -= 1
            right += 1
        return True
            
        