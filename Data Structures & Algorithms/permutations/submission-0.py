class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        toReturn = []
        cur = []

        def create(l):
            if len(l) == 0:
                toReturn.append(cur.copy())
                return
            else:
                for i in range(len(l)):
                    cur.append(l[i])
                    num = l[i]
                    l.remove(num)
                    create(l)
                    l.insert(i, num)
                    cur.pop()
        
        create(nums)
        return toReturn