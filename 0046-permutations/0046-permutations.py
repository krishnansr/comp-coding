class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        all_permutations = []

        # Can solve this using either BFS or DFS.
        # Time complexity: O(E + V) in graph which is O(N!*N).
        # Space complexity: O(N!).
        queue = [(nums, [])]  # Stack contains leftover_numbers, resultant_path.
        while queue:
            curr_nums, curr_path = queue.pop(0)
            if not curr_nums:  # No nums to iterate on.
                all_permutations.append(curr_path)
            
            for i in range(len(curr_nums)):
                updated_nums = curr_nums[:i] + curr_nums[i + 1:]
                updated_path = curr_path + [curr_nums[i]]
                queue.append((updated_nums, updated_path))
        
        return all_permutations                