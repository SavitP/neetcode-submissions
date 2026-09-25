class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        cur = []
        def explore(l):
            if len(l) < k - len(cur):
                return
            if len(cur) == k:
                res.append(cur.copy())
                return
            for i in range(len(l)):
                cur.append(l[i])
                explore(l[i+1:])
                cur.pop()
        lis = [i for i in range(1, n+1)]
        explore(lis)
        return res

