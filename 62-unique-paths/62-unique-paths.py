class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m is 1 or n is 1:
            return 1

        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[0][1] = dp[1][0] = 1

        for i in range(m):
            for j in range(n):
                if i + j > 1:
                    from_left = dp[i][j-1] if j-1 >= 0 else 0
                    from_top = dp[i-1][j] if i-1 >= 0 else 0
                    dp[i][j] = from_left + from_top

        print(dp)
        return dp[-1][-1]