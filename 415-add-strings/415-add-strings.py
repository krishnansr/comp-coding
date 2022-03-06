class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        res = ""
        carry = 0

        len1 = len(num1)
        len2 = len(num2)
        max_len = max(len1, len2)
        for i in range(1, max_len+1):
            digit1 = 0 if i > len1 else num1[-i]
            digit2 = 0 if i > len2 else num2[-i]

            add_val = int(digit1) + int(digit2) + carry
            carry, digit = add_val // 10, add_val % 10
            res = str(digit) + res

        if carry:
            res = '1' + res
        return res