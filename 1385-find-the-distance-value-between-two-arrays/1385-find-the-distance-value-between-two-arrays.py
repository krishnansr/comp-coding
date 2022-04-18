class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        return sum([all([ abs(x1 - x2) > d for x2 in arr2]) for x1 in arr1])