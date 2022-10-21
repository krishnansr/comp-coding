class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_idx = 0

        for i, n in enumerate(nums):
            if i > max_idx:
                return False
            max_idx = max(max_idx, i + n)

        return True

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