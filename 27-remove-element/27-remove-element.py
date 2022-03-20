class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == val:
                nums[i], nums[k] = nums[k], nums[i]
                k -= 1
        return k + 1