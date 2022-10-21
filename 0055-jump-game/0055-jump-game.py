class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [0] * len(nums)
        dp[0] = 1

        for i, n in enumerate(nums):
            if dp[-1]:
                return True
            for j in range(i + 1, min(i + n + 1, len(nums))):
                dp[j] = 1
            if dp[i + 1] == 0:
                return False

    def canJump_rec(self, nums: List[int]) -> bool:
        can_jump = [False]

        def dfs(curr_index):
            if can_jump[0]:
                return
            if curr_index + 1 >= len(nums):
                can_jump[0] = True
                return
            for i in range(nums[curr_index]):
                dfs(curr_index + i + 1)

        dfs(0)
        return can_jump[0]