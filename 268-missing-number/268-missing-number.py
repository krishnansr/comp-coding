class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        num_range = len(nums)
        return (num_range*(num_range+1))//2 - sum(nums)