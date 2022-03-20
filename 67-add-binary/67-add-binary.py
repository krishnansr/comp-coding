class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        digits = ''
        len_a = len(a)
        len_b = len(b)

        for i in range(1, max(len_a, len_b) + 1):
            a_i = 0 if i > len_a else int(a[-i])
            b_i = 0 if i > len_b else int(b[-i])

            _sum = a_i + b_i + carry
            digits, carry = str(_sum % 2) + digits, _sum // 2

        return '1' + digits if carry else digits