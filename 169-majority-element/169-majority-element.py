class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res, diff_count = 0, 0
        for n in nums:
            if diff_count == 0:
                res = n
            diff_count += (1 if res == n else -1)
        return res
        
    def majorityElement_desc(self, nums: List[int]) -> int:
        diff_count = 0
        res = nums[0]
        
        for n in nums:
            if n == res:
                diff_count += 1
            elif diff_count == 0:
                res = n
                diff_count = 1
            else:
                diff_count -= 1
        return res