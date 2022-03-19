class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        return floor(round(exp(log(x) / 2), 8))