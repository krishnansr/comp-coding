class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # two pointer
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                return mid
        return -1
    
    def search_recursion(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            return 0 if nums[0] == target else -1

        mid = len(nums) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            return self.search(nums[:mid], target)
        else:
            retval = self.search(nums[mid:], target)
            if retval != -1:
                retval += mid
            return retval
