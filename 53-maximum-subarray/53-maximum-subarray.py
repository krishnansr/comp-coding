class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # kadane's algorithm
        
        max_sum = nums[0]
        curr_sum = 0
        for n in nums:
            curr_sum = max(0, curr_sum)
            curr_sum += n
            max_sum = max(max_sum, curr_sum)
        return max_sum