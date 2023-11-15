class Solution:
    def rob(self, nums: List[int]) -> int:
        # Since House[1] and House[n] are adjacent, they cannot be robbed together. 
        # Therefore, the problem becomes to rob either House[1]-House[n-1] or House[2]-House[n], depending on which choice offers more money. 
        # Now the problem has degenerated to the House Robber, which is already been solved.
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