class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        toReturn = []
        cur = []

        def create():
            if len(nums) == 0:
                toReturn.append(cur.copy())
                return
            else:
                for i in range(len(nums)):
                    cur.append(nums[i])
                    num = nums[i]
                    nums.remove(num)
                    create()
                    nums.insert(i, num)
                    cur.pop()
        
        create()
        return toReturn