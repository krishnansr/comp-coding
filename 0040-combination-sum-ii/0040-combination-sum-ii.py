class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        cnt = Counter(candidates)
        combinations = []
        
        def dfs(nums, target, path, num_cnt):
            if target == 0:
                combinations.append(path)
                return
            elif target > 0:
                if num_cnt < cnt[nums[0]]:  # check max allowed count
                    dfs(nums, target - nums[0], path + [nums[0]], num_cnt + 1)

                for i in range(1, len(nums)):
                    dfs(nums[i:], target - nums[i], path + [nums[i]], 1)
        
        dfs(list(set(candidates)), target, [], 0)
        return combinations