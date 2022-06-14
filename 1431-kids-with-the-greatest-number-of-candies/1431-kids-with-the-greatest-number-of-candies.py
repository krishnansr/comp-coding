class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        high_enough = max(candies) - extraCandies
        return [c >= high_enough for c in candies]