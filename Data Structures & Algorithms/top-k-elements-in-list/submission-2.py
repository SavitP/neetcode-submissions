class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        for num in nums:
            map[num] = 1 + map.get(num, -1)
        ls = []
        for i in range(len(nums)):
            ls.append([])
        for key in map.keys():
            ls[map.get(key)].append(key)
        ls = ls[::-1]
        toReturn = []
        for ls1 in ls:
            for num in ls1:
                if (len(toReturn) == k):
                    return toReturn
                toReturn.append(num)
        return toReturn
            