class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        counter = {}
        res = 0
        for n in nums:
            curr = counter.get(n, 0)
            if curr:
                res += curr
                counter[n] += 1  # todo
            else:
                counter[n] = 1
        return res