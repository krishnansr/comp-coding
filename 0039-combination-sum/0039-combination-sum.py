class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        combinations = []

        def dfs(nums, target, path):
            if target == 0:
                combinations.append(path)
                return
            elif target > 0:
                for i in range(len(nums)):
                    dfs(nums[i:], target - nums[i], path + [nums[i]])  # send updated target sum
        
        dfs(candidates, target, [])
        return combinations