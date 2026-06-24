class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)
        while True:
            if l + 1 == r and nums[l] != target:
                return -1
            mid = l + (r - l) // 2
            if (nums[mid] == target):
                return mid
            elif (nums[mid] < target):
                l = mid
            else:
                r = mid

            