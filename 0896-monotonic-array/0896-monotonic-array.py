class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        monotonic = True
        dir_flag = 0
        
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                if dir_flag != 2:
                    dir_flag = 1
                else:
                    monotonic = False
                    break
    
            elif nums[i] < nums[i - 1]:
                if dir_flag != 1:
                    dir_flag = 2
                else:
                    monotonic = False
                    break
            
        return monotonic