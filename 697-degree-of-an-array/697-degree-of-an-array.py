class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        first_seen, counter = {}, {}
        degree, res = 0, 0

        for i, n in enumerate(nums):
            first_seen.setdefault(n, i)
            counter[n] = counter.get(n, 0) + 1

            if counter[n] > degree:
                degree = counter[n]
                res = i - first_seen[n] + 1
            elif counter[n] == degree:
                res = min(res, i - first_seen[n] + 1)

        return res