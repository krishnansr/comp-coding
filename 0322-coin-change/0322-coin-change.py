class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # So many edge cases to handle in this bottom-up DP solution.
        # O(T.N) where T is the amount
        # Edge cases: 1. amount not matching with coins
        # 2. 0 amount, 3. 0 coins, 4. starting coin is more than amount
        # 5. ending coin is more than amount 6. happy path
        
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