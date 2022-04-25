class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        max1, max2, res = float('-inf'), float('-inf'), -1
        for i, n in enumerate(nums):
            if n > max1:
                max1, max2 = n, max1
                res = i
            elif n > max2:
                max2 = n
        return res if max1 >= (max2 * 2) else -1
            