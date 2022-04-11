class Solution:
    def findGCD(self, nums: List[int]) -> int:
        minn, maxn = nums[0], nums[0]
        
        for n in nums:
            minn = min(minn, n)
            maxn = max(maxn, n)
        
        return gcd(minn, maxn)