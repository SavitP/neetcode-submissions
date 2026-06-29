class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)
        if (nums[0] < nums[len(nums) - 1] or len(nums) == 1):
            return nums[0]
        while l != r:
            mid = l + (r - l) // 2
            if nums[mid] < nums[mid - 1]:
                return nums[mid]
            if nums[mid] < nums[l]:
                r = mid
            else:
                l = mid
        return nums[r]