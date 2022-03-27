class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # get contiguous block, split into zeros, then find max len
        return max(map(len, ''.join(map(str, nums)).split('0')))