class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # Small tweak from https://leetcode.com/problems/subsets/
        # Using binary based approach doesn't work need to keep track of nums.
        nums.sort()  # Easier to skip duplicates once sorted.
        power_set = []

        # Solution using BFS, also works with DFS.
        queue = [([], nums)]  # (path, rem_nums)
        while queue:
            path, rem_nums = queue.pop(0)
            power_set.append(path)

            for i, n in enumerate(rem_nums):
                if i > 0 and rem_nums[i] == rem_nums[i - 1]:
                    continue
                queue.append((path + [n], rem_nums[i + 1:]))

        return power_set
