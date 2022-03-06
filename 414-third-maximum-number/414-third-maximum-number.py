class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        min_value = float("-inf")
        max1 = max2 = res = min_value

        for i in nums:
            if i > max1:
                max1, max2, res = i, max1, max2
            elif max2 < i < max1:
                max1, max2, res = max1, i, max2
            elif res < i < max2:
                res = i

        if res != min_value:
            return res
        else:
            return max1