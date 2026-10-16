class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}
        def explore(i, buy):
            if i >= len(prices):
                return 0
            if (i, buy) in dp:
                return dp[(i, buy)]
            don = explore(i + 1, buy)
            if buy:
                s = max(don, explore(i + 1, False) - prices[i])
                dp[(i, buy)] = s
                return s
            else:
                s = max(don, explore(i + 2, True) + prices[i])
                dp[(i, buy)] = s
                return s

        return explore(0, True)