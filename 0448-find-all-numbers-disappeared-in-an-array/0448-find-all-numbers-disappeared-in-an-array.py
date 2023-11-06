class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            num_ind = abs(nums[i]) - 1
            if nums[num_ind] > 0:
                nums[num_ind] = -nums[num_ind]
        
        res = []
        for i,n in enumerate(nums):
            if n > 0:
                res.append(i+1)
        
        return res