class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k == 0 or len(nums) == 1:
            return False
        k = min(len(nums) - 1, k)
        
        window_set = set(nums[:k + 1])
        for i, num in enumerate(nums[k + 1:]):
            if len(window_set) != k + 1:
                return True  # there's been a duplicate in the window
            window_set.remove(nums[i])
            window_set.add(num)
            
        return len(window_set) != k + 1