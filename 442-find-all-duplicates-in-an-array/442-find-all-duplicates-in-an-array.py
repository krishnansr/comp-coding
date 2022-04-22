class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        dupes = []
        for num in nums:
            index = abs(num) - 1
            if nums[index] < 0:
                dupes.append(index + 1)
            nums[index] = -nums[index]
        
        return dupes