class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        hash_set = set()
        max_sum = 0
        curr_sum = 0
        
        l, r = 0, 0
        while r < len(nums):
            if nums[r] in hash_set or r - l > k - 1:
                # Found a duplicate element in current window.
                hash_set.remove(nums[l])
                curr_sum -= nums[l]
                l += 1
                continue
            else:  
                # Found a distinct element in current window.
                hash_set.add(nums[r])
                curr_sum += nums[r]
                r += 1 	

            if r - l == k:
                max_sum = max(max_sum, curr_sum)

        return max_sum
