class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = float("-inf")
        i, j = 0, len(height) - 1
        
        while i < j:
            max_area = max(max_area, (min(height[j], height[i])) * (j - i))
            if height[i] > height[j]:
                j -= 1
            else:
                i += 1
        return max_area