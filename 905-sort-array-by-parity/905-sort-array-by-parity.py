class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        i = 0
        for j in range(len(nums)):
            if not nums[j] & 1:
                if i != j:
                    nums[i], nums[j] = nums[j], nums[i]
                i += 1
        return nums
        
    def sortArrayByParity_2pointer(self, nums: List[int]) -> List[int]:
        i, j = 0, len(nums) - 1
        while i < j:
            while i < j and not nums[i] & 1:
                i += 1
            while i < j and nums[j] & 1:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1

        return nums
    
    def sortArrayByParity_sort(self, nums: List[int]) -> List[int]:
        return sorted(nums, key=lambda x: x & 1)