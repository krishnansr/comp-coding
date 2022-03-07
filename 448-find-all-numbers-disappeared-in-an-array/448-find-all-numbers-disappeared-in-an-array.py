class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        rem_nums = set(range(1, len(nums)+1))
        for i in nums:
            if i in rem_nums:
                rem_nums.remove(i)
        return list(rem_nums)