class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = r = len(nums) + 1
        i = 0
        while i < len(nums):
            if nums[i] == 0:
                if i > l:  # swap with 1
                    nums[i], nums[l] = nums[l], nums[i]
                    l = l + 1
                    continue
                elif i > r:  # swap with 2
                    nums[i], nums[r] = nums[r], nums[i]
                    r = r + 1

            elif nums[i] == 1:
                l = min(l, i, r)
                if i > r:
                    nums[i], nums[r] = nums[r], nums[i]
                    r = r + 1
            else:  # 2 val
                r = min(r, i)
                
            i += 1
        return nums