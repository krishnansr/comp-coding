class Solution:
    def rob(self, nums: List[int]) -> int:
        # detailed explanation in https://leetcode.com/problems/house-robber/solutions/156523/from-good-to-great-how-to-approach-most-of-dp-problems/
        # similar to fibonacci (or) climbing 1-2 steps in ladder

        prev1 = 0
        prev2 = 0
        for n in nums:
            prev1, prev2 = max(prev2 + n, prev1), prev1
        return prev1