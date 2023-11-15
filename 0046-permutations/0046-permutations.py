class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        all_permutations = []

        stack = [(nums, [])]  # Stack contains leftover_numbers, resultant_path.
        while stack:
            curr_nums, curr_path = stack.pop(0)
            if not curr_nums:  # No nums to iterate on.
                all_permutations.append(curr_path)
            
            for i in range(len(curr_nums)):
                updated_nums = curr_nums[:i] + curr_nums[i + 1:]
                updated_path = curr_path + [curr_nums[i]]
                stack.append((updated_nums, updated_path))
        
        return all_permutations                