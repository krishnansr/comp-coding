class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not len(intervals):  # Empty interval list.
            return [newInterval]
            
        # Do binary search to zero-in on the index of insertion.
        l, r = 0, len(intervals) - 1
        while l <= r:
            mid = (l + r) // 2
            mid_start = intervals[mid][0]
            
            if mid_start < newInterval[0]:
                l = mid + 1
            elif mid_start > newInterval[0]:
                r = mid - 1
            else:
                break
        
        # Now expand from mid to merge with neighboring intervals.
        start = mid
        while start > -1 and intervals[start][1] >= newInterval[0]:
            start = start - 1
        
        end = mid
        while end < len(intervals) and intervals[end][0] <= newInterval[1]:
            end = end + 1
        
        if start + 1 == end:  # No overlap.
            intervals.insert(start + 1, newInterval)
        else:  # Overlap.
            new_start = min(intervals[start + 1][0], newInterval[0])
            new_end = max(intervals[end - 1][1], newInterval[1])
            intervals[start + 1: end] = [[new_start, new_end]]

        return intervals