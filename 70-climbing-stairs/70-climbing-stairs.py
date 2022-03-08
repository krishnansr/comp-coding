class Solution:
    @lru_cache(maxsize=50)
    def climbStairs(self, n: int) -> int:
        if n < 4:
            return n
        
        return self.climbStairs(n-1) + self.climbStairs(n-2)