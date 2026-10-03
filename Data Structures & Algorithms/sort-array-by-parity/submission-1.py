class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        c = 0
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                nums[c], nums[i] = nums[i], nums[c]
                c += 1
        return nums