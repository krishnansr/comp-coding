class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # the best meeting/interval is the one that ends early because it allows
        # more time for other meetings/intervals in the future
        # explanation here: https://leetcode.com/problems/non-overlapping-intervals/discuss/276056/Python-Greedy-Interval-Scheduling
        intervals.sort(key=lambda x: x[1])
        
        overlap_cnt = 0
        prev_end = intervals[0][1]
        for start, end in intervals[1:]:
            if start >= prev_end:  # There is no conflict.
                prev_end = end
            else:  # Conflict occurred.
                overlap_cnt += 1
                
        return overlap_cnt