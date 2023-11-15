class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        power_set = []
        
        # Solution using BFS.
        queue = [([], 0)]
        while queue:
            subset, ind = queue.pop(0)
            if ind == len(nums):
                power_set.append(subset)
            else:          
                queue.append((subset, ind + 1))  # 0-case.
                queue.append((subset + [nums[ind]], ind + 1))  # 1-case.
            
        return power_set