class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        toReturn = []
        sub = []

        def dfs(i, sum):
            if sum == target:
                toReturn.append(sub.copy())
            else:
                for j in range(i, len(nums)):
                    if sum + nums[j] <= target:
                        sub.append(nums[j])
                        dfs(j, sum + nums[j])
                        sub.pop()
        
        dfs(0, 0)
        return toReturn

        
        