class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        left_sum, right_sum = 0, sum(nums)

        for i in range(0, len(nums)):
            right_sum -= nums[i]
            if left_sum == right_sum:
                return i
            left_sum += nums[i]
        return -1