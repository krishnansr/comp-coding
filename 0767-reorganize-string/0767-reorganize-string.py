class Solution:
    def reorganizeString(self, name: str) -> str:
        # Simpler solution using heaps. 
        # It is O(N log A) where A is the size of the alphabet in the heap, since it's a constant, overall time is O(N)
        counter = dict()
        for char in name:
            counter[char] = counter.get(char, 0) + 1

        heap = [(-v, k) for k, v in counter.items()]
        heapq.heapify(heap)

        prev_cnt, prev_char = 0, ''
        res = ''
        while heap:
            cnt, char = heapq.heappop(heap)
            res += char
            if prev_cnt < 0:
                # push the element, char from previous call.
                heapq.heappush(heap, (prev_cnt, prev_char))
            cnt += 1
            prev_cnt, prev_char = cnt, char  # keep remembering for next call.
        
        return res if len(res) == len(name) else ''

    def reorganizeString_sort(self, name: str) -> str:
        # Simpler solution using sort -> Time is O(N log N).
        # Solution from https://leetcode.com/problems/reorganize-string/discuss/113435/4-lines-Python
        if len(name) < 2:
            return name
        
        ls = sorted(sorted(name), key= name.count) 
        mid = len(ls) // 2
        ls[1::2], ls[::2] = ls[:mid], ls[mid:]
        
        return ''.join(ls) if ls[-1] != ls[-2] else ''