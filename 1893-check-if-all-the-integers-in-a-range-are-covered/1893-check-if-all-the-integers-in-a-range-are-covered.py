class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        arr = [False] * (right - left + 1)
        for l, r in ranges:
            l -= left
            r -= left

            if r >= 0 and l < len(arr):
                l = max(l, 0)
                r = min(r, len(arr) - 1)
                arr[l: r + 1] = repeat(True, r + 1 - l)

        return sum(arr) == len(arr)