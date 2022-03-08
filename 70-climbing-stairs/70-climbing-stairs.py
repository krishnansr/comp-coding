class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 4:
            return n

        prev = 0
        fib = 1
        for _ in range(n):
            _sum = prev + fib
            prev = fib
            fib = _sum
        return fib
            
    
    # @lru_cache(maxsize=50)
    def climbStairs_cached(self, n: int) -> int:
        if n < 4:
            return n
        return self.climbStairs(n-1) + self.climbStairs(n-2)