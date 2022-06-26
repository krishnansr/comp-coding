class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        counter = [0] * 1001
        for ls in nums:
            for n in ls:
                counter[n] += 1
        
        return [i for i, x in enumerate(counter) if x == len(nums)]