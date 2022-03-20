class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for i in range(len(digits) - 1, -1, -1):
            _sum = digits[i] + carry
            digits[i], carry = _sum % 10, _sum // 10

        return [1] + digits if carry else digits