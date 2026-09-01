class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        toReturn = []
        nums.sort()
        cur = []

        def create(start):
            toReturn.append(cur.copy())
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                cur.append(nums[i])
                create(i + 1)
                cur.pop()

        create(0)
        return toReturn