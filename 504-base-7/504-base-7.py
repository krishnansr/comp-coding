class Solution:
    def convertToBase7(self, num: int) -> str:
        sign, num, res = num < 0, abs(num), ''
        
        while num:
            res = str(num % 7) + res
            num //= 7

        return '-' * sign + res or "0"
            