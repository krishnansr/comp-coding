class Solution:
    log_four = log10(4)
    
    def isPowerOfFour(self, n: int) -> bool:
        if n < 1:
            return False
        return (log10(n) / self.log_four).is_integer()