class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # variant of the 3-sum problem, can't do better than O(N^2)
        # per CS theory https://en.wikipedia.org/wiki/3SUM
        
        nums.sort()
        
        res = sum(nums[:3])
        res_diff = abs(res - target)
        
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                # to avoid duplicates in 3 sum
                continue
            
            l, r = i + 1, len(nums) - 1
            while l < r:
                curr_sum = nums[i] + nums[l] + nums[r]
                curr_diff = abs(curr_sum - target)
                if curr_diff < res_diff:
                    res = curr_sum
                    res_diff = curr_diff
                
                if curr_sum < target:
                    l += 1
                elif curr_sum > target:
                    r -= 1
                else:  # matches target, closest it can get
                    break                    

        return res
                    