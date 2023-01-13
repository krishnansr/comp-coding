class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        fact_low, fact_high = [], []
        for num in range(1, int(sqrt(n)) + 1):
            if n % num == 0:
                fact_low.append(num)
                fact_high.append(n // num)
        
        if fact_low[-1] == fact_high[-1]:
            fact_high.pop()
            
        all_factors = fact_low + fact_high[::-1]
        return -1 if k > len(all_factors) else all_factors[k - 1]