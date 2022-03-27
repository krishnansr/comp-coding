class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count, curr = 0, 0
        for n in nums + [0]:
            if n:
                curr += 1
            else:
                count = max(count, curr)
                curr = 0
        return count
        
    def findMaxConsecutiveOnes_map(self, nums: List[int]) -> int:
        # get contiguous block, split into zeros, then find max len
        return max(map(len, ''.join(map(str, nums)).split('0')))