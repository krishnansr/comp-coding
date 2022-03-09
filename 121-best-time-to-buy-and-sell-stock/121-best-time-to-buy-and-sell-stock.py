class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        profit_stonks = 0

        for day in prices[1:]:
            if day < buy:
                buy = day
                continue
            elif day - buy > profit_stonks:
                profit_stonks = day - buy  # new profit stonks /|/^

        return profit_stonks