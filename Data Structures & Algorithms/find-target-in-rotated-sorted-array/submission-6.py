class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = self.findMin(nums)
        print(start)
        l = 0
        r = start
        if len(nums) == 1 and nums[0] != target:
            return -1
        while (l + 1 != r or nums[l] == target) and l != r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                r = mid
            else:
                l = mid
        if nums[l] == target:
            return l
        l = start
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

    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        while l != r:
            mid = l + (r - l) // 2
            if nums[mid] < nums[mid - 1]:
                mid
            if nums[mid] < nums[r]:
                r = mid
            else:
                l = mid + 1
        return l