class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}  # Set of (index, total_at_that_index) for memoization.
        def backtrack(i, total):
            if i == len(nums):
                return int(total == target)
            elif (i, total) in dp:
                return dp[(i, total)]

            dp[(i, total)] = backtrack(i + 1, total + nums[i]) + backtrack(i + 1, total - nums[i])
            return dp[(i, total)]
        return backtrack(0, 0)

    
    def findTargetSumWays2(self, nums: List[int], target: int) -> int:
        # O(N. T) solution where T is the sum(nums)
        # solution explanation: https://youtu.be/g0npyaQtAQM
        dp = {}  # set

        def backtracking(i, total):
            if i == len(nums):
                return int(total == target)
            if (i, total) in dp:
                return dp[(i, total)]
            
            dp[(i, total)] = backtracking(i + 1, total + nums[i]) + \
                             backtracking(i + 1, total - nums[i])
            return dp[(i, total)]
    
        return backtracking(0, 0)
    
    
    def findTargetSumWays_bfs(self, nums: List[int], target: int) -> int:
        # naive solution using BFS/DFS that is O(2^N)
        num_ways = 0
        
        total = nums[0]
        queue = [(1, total), (1, -total)]
        while queue:
            ind, total = queue.pop(0)
            if ind == len(nums):  # sequence ended
                num_ways += int(total == target)
            else:
                queue.append((ind + 1, total + nums[ind]))
                queue.append((ind + 1, total - nums[ind]))
        return num_ways
