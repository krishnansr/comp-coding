class Solution:
    def numberOfMatches(self, n: int) -> int:
        return n - 1
        
    def numberOfMatches_simulation(self, n: int) -> int:
        num_matches = 0
        while n > 1:
            num_matches += n // 2
            n = (n // 2) + (n & 1)
            
        return num_matches