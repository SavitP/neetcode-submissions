class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        l = [0] * len(cost)
        if len(cost) < 2:
            return 0
        for i in range(2, len(cost)):
            l[i] = min(l[i - 2] + cost[i - 2], l[i-1] + cost[i-1])
        
        return min(l[len(cost) - 2] + cost[len(cost) - 2], l[len(cost)-1] + cost[len(cost)-1])