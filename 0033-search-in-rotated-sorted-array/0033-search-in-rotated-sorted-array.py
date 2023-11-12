class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid

            left_half_is_sorted = nums[l] <= nums[mid]
            target_in_left_half = nums[l] <= target <= nums[mid]
            target_in_right_half = nums[mid] <= target <= nums[r]
            
            if left_half_is_sorted and target_in_left_half:
                r = mid - 1
            elif (not left_half_is_sorted) and (not target_in_right_half):
                r = mid - 1
            else:
                l = mid + 1
        return -1
        
    def search_double_binsearch(self, nums: List[int], target: int) -> int:
        # Find the pivot index in O(log N) time.
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] < nums[r]:  # Right half is ordered.
                r = mid
            else:
                l = mid + 1
            
        if target > nums[-1]:  # Target could be in larger half.
            l, r = 0, mid - 1
        else:  # Target could be in bigger half.
            l, r = mid, len(nums)
        
        # Find the number in O(log N) time.
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                return mid
            
        return -1