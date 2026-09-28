# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l = 0
        while True:
            mid = l + (n - l) // 2
            out = guess(mid)
            if out == 0:
                return mid
            elif out == -1:
                n = mid - 1
            else:
                l = mid + 1