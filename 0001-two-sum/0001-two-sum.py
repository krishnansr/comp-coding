class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        subtrahend_map = {}
        for i, n in enumerate(nums):
          subtrahend = target - n
          
          if subtrahend in subtrahend_map:
            return [subtrahend_map[subtrahend], i]
          subtrahend_map[n] = i
        return [0, 0]