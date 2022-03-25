class Solution:
    def binaryGap(self, n: int) -> int:
        if n & (n - 1) == 0:
            return 0
        
        max_dist, prev = 0, -1
        for i, b in enumerate(bin(n)[3:]):
            if b == '1':
                max_dist = max(max_dist, i - prev)
                prev = i
        return max_dist