class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        i, j = 0, 1
        while i < len(nums) and j < len(nums):
            while i < len(nums) and nums[i] & 1 == 0:
                i += 2
            while j < len(nums) and nums[j] & 1 == 1:
                j += 2
            else:
                if i < len(nums) and j < len(nums):
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 2
                    j += 2
        return nums