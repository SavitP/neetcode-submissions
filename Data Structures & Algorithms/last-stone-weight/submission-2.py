class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = []
        for stone in stones:
            heapq.heappush_max(max_heap, stone)
        while len(max_heap) > 1:
            s1 = heapq.heappop_max(max_heap)
            s2 = heapq.heappop_max(max_heap)
            if s1 != s2:
                s1 -= s2
                heapq.heappush_max(max_heap, s1)
        if len(max_heap) == 0:
            return 0
        return heapq.heappop_max(max_heap)