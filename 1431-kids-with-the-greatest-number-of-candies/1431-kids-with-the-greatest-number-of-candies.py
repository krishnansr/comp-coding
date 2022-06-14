class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_cand = max(candies)
        return [c + extraCandies >= max_cand for c in candies]