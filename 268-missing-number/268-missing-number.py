class Solution:
    def missingNumber_bitwise(self, nums: List[int]) -> int:
        return reduce(lambda i, j: i^j, nums + list(range(len(nums)+1)), 0)
    
    
    def missingNumber(self, nums: List[int]) -> int:
        num_range = len(nums)
        return (num_range*(num_range+1))//2 - sum(nums)