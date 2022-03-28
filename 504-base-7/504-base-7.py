class Solution:
    def convertToBase7(self, num: int) -> str:
        sign = num < 0
        num, res = abs(num), ''
        
        while num:
            res = str(num % 7) + res
            num //= 7

        return '-' * sign + res or "0"
            