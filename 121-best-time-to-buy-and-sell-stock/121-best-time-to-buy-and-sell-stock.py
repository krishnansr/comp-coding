class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        profit_stonks = 0

        for day in prices[1:]:
            if day < buy:
                buy = day
            _profit = day - buy
    
            if _profit > profit_stonks:
                profit_stonks = _profit  # new profit stonks /|/^

        return profit_stonks