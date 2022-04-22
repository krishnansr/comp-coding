class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        dupes = []
        for num in nums:
            if nums[abs(num) - 1] < 0:
                dupes.append(abs(num))
            nums[abs(num) - 1] *= -1
        
        return dupes