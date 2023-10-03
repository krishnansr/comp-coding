class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # similar questions https://leetcode.com/problems/merge-intervals/discuss/21227/7-lines-easy-Python/237941
        intervals.sort(key= lambda x: x[0])
        out = [intervals[0]]
        
        for interval in intervals[1:]:
            prev_high = out[-1][-1]
            
            if interval[0] <= prev_high:
                out[-1][-1] = max(interval[1], prev_high)
            else:
                out.append(interval)
        return out