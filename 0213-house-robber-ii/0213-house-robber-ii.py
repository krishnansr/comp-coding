class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        return max(self.normal_rob(nums[:-1]), self.normal_rob(nums[1:]))

    def normal_rob(self, nums: List[int]) -> int:
        # solution from https://leetcode.com/problems/house-robber/
        
        prev_max = 0
        max_money = 0
        for n in nums:
            max_money, prev_max = max(prev_max + n, max_money), max_money
        return max_money