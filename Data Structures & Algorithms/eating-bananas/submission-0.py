class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max = 0
        for ban in piles:
            if ban > max:
                max = ban
        l = 1
        r = max + 1
        while l != r:
            mid = l + (r - l) // 2
            if self.canComplete(piles, mid, h):
                r = mid
            else:
                l = mid + 1
        if self.canComplete(piles, l, h):
            return l
        else:
            return l + 1
            

    def canComplete(self, piles: List[int], k: int, h: int) -> bool:
        time = 0
        for ban in piles:
            time += math.ceil(ban / k)
        return time <= h
