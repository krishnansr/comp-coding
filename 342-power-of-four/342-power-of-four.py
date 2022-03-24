class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n > 0 and (n & (n-1) == 0) and (n.bit_length() & 1)
        
    def isPowerOfFour_log(self, n: int) -> bool:
        if n < 1:
            return False
        return (log10(n) / log10(4)).is_integer()