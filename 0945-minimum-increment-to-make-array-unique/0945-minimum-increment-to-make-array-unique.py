class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        # using Union find - https://leetcode.com/problems/minimum-increment-to-make-array-unique/solutions/197687/java-c-python-straight-forward/
        roots = {}
        def find(x):
            if x in roots:
                roots[x] = find(roots[x] + 1)
            else:
                roots[x] = x
            return roots[x]

        moves = 0
        for n in nums:
            moves += find(n) - n
        return moves
