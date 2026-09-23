class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return nums[0]
        if len(nums) < 3:
            return max(nums[0], nums[1])
        if len(nums) < 4:
            return max(nums[0] + nums[2], nums[1])
        nums[2] = max(nums[0] + nums[2], nums[1])
        for i in range(3, len(nums)):
            nums[i] += max(nums[i - 2], nums[i - 3])
        return max(nums[len(nums) - 1], nums[len(nums) - 2])
            