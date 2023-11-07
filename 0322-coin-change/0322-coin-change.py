class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount is 0:
            return 0

        dp = [0] * amount
        for coin in coins:
            if coin - 1 < amount:
                dp[coin - 1] = 1  # since we already have that denomination
        
        for i in range(amount):
            # curr_amount = i + 1
            if dp[i] != 0:
                continue  # already set
            
            possible_paths = [dp[i - coin] for coin in coins \
                              if i - coin >= 0 and dp[i - coin] > 0]
            if possible_paths:
                dp[i] = 1 + min(possible_paths)
            else:
                dp[i] = -1
        
        print(dp)
        return dp[-1]