class Solution:
    def findComplement(self, num: int) -> int:
        # bit ^ 1 == ~bit
        return num ^ ((1 << num.bit_length()) - 1)