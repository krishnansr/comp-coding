class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        return min([y - x for x, y in zip(nums, nums[k - 1:])])
