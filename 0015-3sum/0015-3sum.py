class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # the best you can do is a N^2 time solution
        # sorting helps with not using a O(N) space as in directly
        # using 2-sum
        
        nums.sort()
        
        res = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                # to avoid duplicates in 3 sum
                continue
            if nums[i] > 0:
                break
            
            target = - nums[i]
            l, r = i + 1, len(nums) - 1
            while l < r:
                if nums[l] + nums[r] < target:
                    l += 1
                elif nums[l] + nums[r] > target:
                    r -= 1
                else:  # matches target
                    res.append([nums[i], nums[l], nums[r]])
                    
                    # handle potential duplicates
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1

        return res
                    
                    
                    
                    
                    