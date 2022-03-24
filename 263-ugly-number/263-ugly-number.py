class Solution:
    def isUgly(self, n: int) -> bool:
        if n < 1:
            return False  # negative nunmbers have -1 and 0 are not ugly
        for factor in [10, 9, 8, 6, 5, 4, 3, 2]:
            while n % factor == 0:
                n /= factor     
        return n == 1