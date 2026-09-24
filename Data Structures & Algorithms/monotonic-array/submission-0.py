class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        greater = False
        less = False
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                if less:
                    return False
                greater = True
            if nums[i] > nums[i-1]:
                if greater:
                    return False
                less = True
        return True
                    