class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # So many edge cases to handle in this bottom-up DP solution.
        # O(T.N) where T is the amount
        # Edge cases: 1. amount not matching with coins
        # 2. 0 amount, 3. 0 coins, 4. starting coin is more than amount
        # 5. ending coin is more than amount 6. happy path
        
        # Initialize dp array
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0  # 0-th index is base case.
        
        for amt in range(1, amount + 1):
            for coin in coins:
                if amt - coin >= 0:  # If all coins are bigger than amt.            
                    dp[amt] = min(dp[amt], 1 + dp[amt - coin])
        
        min_coins = dp[amount]
        return min_coins if min_coins != amount + 1 else -1
        
    
    def coinChange_diff_init(self, coins: List[int], amount: int) -> int:
        
        if amount is 0:
            return 0

        dp = [0] * amount
        for coin in coins:
            if coin - 1 < amount:  # if amount is less than all coins.
                dp[coin - 1] = 1  # since we already have that denomination.
        
        for i in range(amount):
            if dp[i] != 0:
                continue  # already set
            
            possible_paths = [dp[i - coin] for coin in coins \
                              if i - coin >= 0 and dp[i - coin] > 0]
            if possible_paths:
                dp[i] = 1 + min(possible_paths)
            else:
                dp[i] = -1
        
        return dp[-1]