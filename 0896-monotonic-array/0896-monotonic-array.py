class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if nums[-1] > nums[0]:  # increasing order
            cmp_fn = lambda x, y: x > y
        else:
            cmp_fn = lambda x, y: x < y

        for i in range(1, len(nums)):
            if cmp_fn(nums[i - 1], nums[i]):
                return False
        return True
        
    def isMonotonic_branched(self, nums: List[int]) -> bool:
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