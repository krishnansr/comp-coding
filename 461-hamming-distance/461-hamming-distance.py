class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        # find bits that are different using xor and count them
        return (x ^ y).bit_count()