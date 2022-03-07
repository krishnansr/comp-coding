class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        rem_nums = [True] * len(nums)
        
        for i in nums:
            rem_nums[i-1] = False
        
        return [ind+1 for ind, x in enumerate(rem_nums) if x]