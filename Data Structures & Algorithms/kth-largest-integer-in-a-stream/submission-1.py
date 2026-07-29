class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.l = nums
        self.l.sort()
        self.l.reverse()
        self.k = k

    def add(self, val: int) -> int:
        if len(self.l) == 0:
            self.l.append(val)
        for i in range(len(self.l)):
            if self.l[i] < val:
                self.l.insert(i, val)
                break
        print(self.l)
        if len(self.l) <= self.k:
            return self.l[len(self.l) - 1]
        return self.l[self.k - 1]
