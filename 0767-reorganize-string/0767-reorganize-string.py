class Solution:
    def reorganizeString(self, name: str) -> str:
        # Simpler solution using sort -> Time is O(N log N).
        if len(name) < 2:
            return name
        
        ls = sorted(sorted(name), key= name.count) 
        
        h = len(ls) // 2
        ls[1::2], ls[::2] = ls[:h], ls[h:]
        
        return ''.join(ls) if ls[-1] != ls[-2] else ''
            
    def reorganizeString_heap(self, name: str) -> str:
        # Simpler solution using heaps.
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
                # push the element, char from previous call
                heapq.heappush(heap, (prev_cnt, prev_char))
            cnt += 1
            prev_cnt, prev_char = cnt, char  # keep remembering for next call.
        
        return res if len(res) == len(name) else ''
