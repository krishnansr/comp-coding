class Solution:
    def rob(self, nums: List[int]) -> int:
        # detailed explanation in https://leetcode.com/problems/house-robber/solutions/156523/from-good-to-great-how-to-approach-most-of-dp-problems/
        # similar to fibonacci (or) climbing 1-2 steps in ladder.

        prev_max = 0
        max_money = 0
        for n in nums:
            max_money, prev_max = max(prev_max + n, max_money), max_money
            
        return max_money