class Solution:
    def reorganizeString(self, name: str) -> str:
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
        
    def reorganizeString_heap2(self, name: str) -> str:
        char_counter = dict()
        for char in name:
            char_counter[char] = char_counter.get(char, 0) + 1

        char_count_list = [(-v, k) for k, v in char_counter.items()]
        heapq.heapify(char_count_list)

        modified_string = ''
        while char_count_list:
            count, char = heapq.heappop(char_count_list)
            
            if (not modified_string) or char != modified_string[-1]:
                modified_string += char
                if count < -1:
                    heapq.heappush(char_count_list, (count + 1, char))
            elif char_count_list:
                count2, char2 = heapq.heappop(char_count_list)
                modified_string += char2
                if count2 < -1:
                    heapq.heappush(char_count_list, (count2 + 1, char2))
                heapq.heappush(char_count_list, (count, char))
            else:
                return ''
        
        return modified_string
