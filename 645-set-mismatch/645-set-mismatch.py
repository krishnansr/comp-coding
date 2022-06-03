class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        indices = [0] * len(nums)
        for n in nums:
            indices[n - 1] += 1
        return [j[1] for j in sorted([(x, i + 1) for i, x in enumerate(indices) if x != 1], reverse=True)]
        
    def findErrorNums_math(self, nums: List[int]) -> List[int]:
        set_sum = sum(set(nums))
        new_num = sum(nums) - set_sum
        missing_num = len(nums) * (len(nums) + 1) // 2 - set_sum
        return [new_num, missing_num]