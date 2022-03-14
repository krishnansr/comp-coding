class Solution:
    def check(self, nums: List[int]) -> bool:
        inc_count = 0
        
        prev_num = nums[0]
        for curr_num in nums[1:]:
            if curr_num < prev_num:
                inc_count += 1
            prev_num = curr_num
            
        return (inc_count == 0) or (inc_count == 1 and curr_num <= nums[0])