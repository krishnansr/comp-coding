class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # problem can be re-imagined like 
        # https://leetcode.com/problems/linked-list-cycle-ii/
        slow = nums[0]
        fast = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        fast = nums[0]  # move x steps to get to actual duplicate node
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow
        
    def findDuplicate_extraspace(self, nums: List[int]) -> int:
        return sum(nums) - sum(set(nums))