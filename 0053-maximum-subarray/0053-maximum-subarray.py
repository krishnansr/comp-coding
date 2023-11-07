class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # kadane's algorithm
        
        max_sum = float('-inf')
        curr_sum = 0
        for n in nums:
            curr_sum = max(0, curr_sum)  # additional step than regular max sum
            curr_sum += n
            max_sum = max(max_sum, curr_sum)
        return max_sum
    
    
    def maxSubArray_understandable(self, nums: List[int]) -> int:
        # same as above but more understandable and not concise
        max_sum = float('-inf')	
        curr_sum = 0
        for i, n in enumerate(nums):
            if curr_sum < 0:
                curr_sum = n
            else:
                curr_sum += n
            max_sum = max(max_sum, curr_sum)
        return max_sum

