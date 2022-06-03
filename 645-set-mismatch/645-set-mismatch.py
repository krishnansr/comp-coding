class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        set_sum = sum(set(nums))
        new_num = sum(nums) - set_sum
        missing_num = len(nums) * (len(nums) + 1) // 2 - set_sum
        return [new_num, missing_num]