class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hs = set(nums)
        toReturn = 0
        for num in nums:
            if num - 1 not in hs:
                count = 1
                last = num
                while True:
                    if last + 1 in hs:
                        count += 1
                        last = last + 1
                    else:
                        break
                if count > toReturn:
                    toReturn = count
        return toReturn
        

        