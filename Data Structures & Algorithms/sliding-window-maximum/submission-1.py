class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        toReturn = []
        for i in range(len(nums) - k + 1):
            max = nums[i]
            for j in range(i, i + k):
                if nums[j] > max:
                    max = nums[j]
            toReturn.append(max)
        return toReturn