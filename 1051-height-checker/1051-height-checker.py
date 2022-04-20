class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        return sum([x != y for x, y in zip(heights, sorted(heights))])
    
    def heightChecker_count_sort(self, heights: List[int]) -> int:
        # using count sort - O(n)
        
        cdf_freq = [0] * max(heights)
        for h in heights:
            cdf_freq[h-1] += 1
        for i in range(1, len(cdf_freq)):
            cdf_freq[i] += cdf_freq[i-1]
        
        cnt = 0
        for h in heights:
            cnt += heights[cdf_freq[h-1]-1] != h
            cdf_freq[h-1] -= 1
        
        return cnt