class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num_set = set()
        for i in nums:
            if i not in num_set:
                num_set.add(i)
            else:
                return True
        return False