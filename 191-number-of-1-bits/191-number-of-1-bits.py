class Solution:
    def hammingWeight(self, n: int) -> int:
        if n < 2:
            return n
        
        count = 0
        for _ in range(ceil(log2(n))+1):
            count += n & 1
            n >>= 1

        return count