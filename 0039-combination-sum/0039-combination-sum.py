class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # Another solution using Dynamic Programming
        # https://youtu.be/EM8IgIIiOdY?t=337

        dp = [[] for _ in range(target + 1)]
        dp[0].append([])  # Initialize 0 to Null list.

        for cand in candidates:  # Runs for 2, 3, 5.
            for i in range(cand, target + 1):  # Runs for 2 -> 8, 3 -> 8, 5 -> 8
                for combo in dp[i - cand]:
                    # Only extends if there's a previous combination in dp[i - cand].
                    dp[i].append(combo + [cand])
        
        return dp[-1]
    
    
    def combinationSum_backtrack(self, candidates: List[int], target: int) -> List[List[int]]:
        combinations = []

        # Depth-First search is a specific form of backtracking 
        # related to searching tree structures.
        # Backtracking is a more general purpose algorithm.
        # Backtracking is usually implemented as DFS plus search pruning
        def dfs(nums, target, path):
            if target == 0:
                combinations.append(path)
                return
            elif target > 0:
                for i in range(len(nums)):
                    dfs(nums[i:], target - nums[i], path + [nums[i]])  # send updated target sum
        
        dfs(candidates, target, [])
        return combinations