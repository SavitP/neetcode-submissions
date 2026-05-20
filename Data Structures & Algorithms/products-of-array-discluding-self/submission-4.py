class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prec = []
        prectot = 1
        for i in range(len(nums)):
            prec.append(prectot)
            prectot *= nums[i]
        suc = []
        suctot = 1
        for i in range(len(nums) - 1, -1, -1):
            suc.insert(0, suctot)
            suctot *= nums[i]
        toReturn = []
        for i in range(len(nums)):
            toReturn.append(prec[i] * suc[i])
        return toReturn
