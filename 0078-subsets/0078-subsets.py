class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # Easier to skip duplicates once sorted.
        power_set = []

        # Solution using BFS, also works with DFS.
        queue = [([], nums)]  # (path, rem_nums)
        while queue:
            path, rem_nums = queue.pop(0)
            power_set.append(path)

            for i, n in enumerate(rem_nums):
                queue.append((path + [n], rem_nums[i + 1:]))

        return power_set
    
    def subsets_binary_approach(self, nums: List[int]) -> List[List[int]]:
        power_set = []
        
        # Solution using BFS, also works with DFS.
        queue = [([], 0)]
        while queue:
            subset, ind = queue.pop(0)
            if ind == len(nums):
                power_set.append(subset)
            else:          
                queue.append((subset, ind + 1))  # 0-case.
                queue.append((subset + [nums[ind]], ind + 1))  # 1-case.
            
        return power_set