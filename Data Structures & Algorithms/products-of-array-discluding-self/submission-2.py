class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeros = 0
        total = 0
        for num in nums:
            if (num != 0):
                if (total == 0):
                    total += 1
                total *= num
            else:
                zeros += 1
        toReturn = []
        if (zeros > 1):
            for num in nums:
                toReturn.append(0)
            return toReturn
        for num in nums:
            if (num == 0):
                toReturn.append(total)
            else:
                if (zeros > 0):
                    toReturn.append(0)
                else:
                    toReturn.append(int(total / num))
        return toReturn
        