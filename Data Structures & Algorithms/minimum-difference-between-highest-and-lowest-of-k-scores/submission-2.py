class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if k == 1:
            return 0
        nums.sort()
        l = 0
        r = k - 1
        if k == len(nums):
            return nums[k - 1]- nums[0]
        m = nums[k] - nums[0]
        while r < len(nums):
            print(nums[r])
            m = min(m, nums[r] - nums[l])
            l += 1
            r += 1
        return m