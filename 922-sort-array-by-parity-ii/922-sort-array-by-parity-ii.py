class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            if i & 1 == nums[i] & 1:
                continue

            j = len(nums) - 1
            while nums[j] & 1 == nums[i] & 1:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]

        return nums