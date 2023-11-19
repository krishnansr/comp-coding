class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
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
        
        visited = set()
        max_cluster = 0
        for num in nums:
            # Visit the unvisited numbers.
            if num not in visited:
                visited.add(num)
                curr_cluster  = dfs(num)
                max_cluster = max(max_cluster, curr_cluster)

        return max_cluster