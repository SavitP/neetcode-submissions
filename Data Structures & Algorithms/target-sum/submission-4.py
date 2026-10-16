class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        mem = {}
        def explore(i, tot):
            if i == len(nums):
                if tot == target:
                    return 1
                else:
                    return 0
            if (i, tot) in mem:
                return mem[(i, tot)]
            s = explore(i + 1, tot + nums[i]) + explore(i + 1, tot - nums[i])
            mem[(i, tot)] = s
            return s
        return explore(0, 0)
            
