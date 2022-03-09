class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        profit_stonks = 0

        for day in prices[1:]:
            if day < buy:
                buy = day
            _profit = day - buy
            profit_stonks = max(profit_stonks, _profit)

        return profit_stonks