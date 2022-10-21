class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # binary search explanation in https://leetcode.com/problems/longest-increasing-subsequence/discuss/1326308/C++Python-DP-Binary-Search-BIT-Solutions-Picture-explain-O(NlogN)
        sub = []
        for n in nums:
            if len(sub) == 0 or sub[-1] < n:
                sub.append(n)
            else:
                sub_idx = bisect_left(sub, n)
                sub[sub_idx] = n
        return len(sub)
        
    def lengthOfLIS_dp(self, nums: List[int]) -> int:
        # dp solution is O(n^2) doesn't work
        lis = [1] * len(nums)
        for i in range(len(nums))[::-1]:
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    lis[i]  = max(lis[i], lis[j] + 1)
        return max(lis)