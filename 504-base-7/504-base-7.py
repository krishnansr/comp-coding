class Solution:
    def convertToBase7(self, num: int) -> str:
        if not num:
            return str(num)
        
        sign, num = num < 0, abs(num)
        res, carry = '', 0
        while num:
            num, carry = num // 7, num % 7
            res = str(carry) + res

        return '-' * sign + res
            