class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify_max(nums)
        toReturn = 0
        for i in range(k):
            toReturn = heapq.heappop_max(nums)
        return toReturn