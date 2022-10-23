class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        # using Union find - https://leetcode.com/problems/minimum-increment-to-make-array-unique/solutions/197687/java-c-python-straight-forward/
        
        roots = {}
        def find(x):
            roots[x] = find(roots[x] + 1) if x in roots else x
            return roots[x]

        return sum(find(n) - n for n in nums)
