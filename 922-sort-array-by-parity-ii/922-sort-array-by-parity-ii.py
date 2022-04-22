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
    
    def sortArrayByParityII_search(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            if i & 1 == nums[i] & 1:
                continue

            j = len(nums) - 1
            while nums[j] & 1 == nums[i] & 1:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]

        return nums