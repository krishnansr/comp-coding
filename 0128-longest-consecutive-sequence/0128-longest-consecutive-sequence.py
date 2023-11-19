class Solution:
    def longestConsecutive(self, nums):
        # Credit to https://leetcode.com/problems/longest-consecutive-sequence/discuss/41057/Simple-O(n)-with-Explanation-Just-walk-each-streak

        num_set = set(nums)  # O(N) space and time.
        max_size = 0
        for num in num_set:
            # Check if it's the starting number
            if num - 1 not in num_set:
                y = num + 1
                while y in num_set:
                    y += 1
                max_size = max(max_size, y - num)
        return max_size
    
    def longestConsecutive_clustering(self, nums: List[int]) -> int:
        # build an adjacency map in O(N) time.
        adj_map = dict()
        for num in nums:
            neighbors = set()
            if num - 1 in adj_map:
                adj_map[num - 1].add(num)
                neighbors.add(num - 1)
            if num + 1 in adj_map:
                adj_map[num + 1].add(num)
                neighbors.add(num + 1)

            adj_map[num] = neighbors
        
        # Now traverse through neighbors and find biggest cluster (like clustering problem)
        def dfs(num):
            total = 0
            for neighbor in adj_map[num]:
                # Visit the unvisited neighbors.
                if neighbor not in visited:
                    visited.add(neighbor)
                    total += dfs(neighbor)
            return total + 1
        
        # This visited set is a must, can't skip for clustering.
        visited = set()
        max_cluster = 0
        for num in nums:
            # Visit the unvisited numbers.
            if num not in visited:
                visited.add(num)
                curr_cluster  = dfs(num)
                max_cluster = max(max_cluster, curr_cluster)

        return max_cluster