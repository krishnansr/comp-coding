class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_sum = -nums[-1]
        right_sum = sum(nums)

        for i in range(0, len(nums)):
            left_sum += nums[i - 1]
            right_sum -= nums[i]
            if left_sum == right_sum:
                return i
        return -1