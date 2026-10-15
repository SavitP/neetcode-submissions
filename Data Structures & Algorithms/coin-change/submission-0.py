class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def explore(a):
            if a == 0:
                return 0
            if a in memo:
                return memo[a]
            res = 1e9
            for c in coins:
                    if a - c >= 0:
                        res = min(res, 1 + explore(a - c))
            memo[a] = res
            return res

        to = explore(amount);
        if to == 1e9:
            return -1
        return to
