class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i, n = 0, len(nums)
        for j in range(n):
            if nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1