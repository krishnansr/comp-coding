class Solution:
    max_pow = 3 ** 20
    def isPowerOfThree(self, n: int) -> bool:
        return n > 0 and self.max_pow % n == 0
    
    
    def isPowerOfThree_log(self, n: int) -> bool:
        if n < 1:
            return False
        return (log10(n) / log10(3)).is_integer()