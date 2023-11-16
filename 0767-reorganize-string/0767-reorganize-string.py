class Solution:
    def reorganizeString(self, name: str) -> str:
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
