class Solution:
    def lengthOfLongestSubstring(self, string: str) -> int:
        # Explanation from https://youtu.be/EM8IgIIiOdY?t=154
        char_set = set()
        max_length = 0
        
        l, r = 0, 0
        while r < len(string):
            
            if string[r] not in char_set:
                # New char, expand the sliding window.
                char_set.add(string[r])
                r += 1
                max_length = max(max_length, r - l)
            else:
                # Duplicate char, shrink the sliding window.
                # Keep moving l up until duplicate of r is removed.
                char_set.remove(string[l])
                l += 1
            
        return max_length

    def lengthOfLongestSubstring_hashmap(self, s: str) -> int:
        char_dict = dict()
        seq_start = -1
        max_length = 0
        
        for ind, char in enumerate(s):
            if char in char_dict and seq_start <= char_dict[char]:
                seq_start = char_dict[char]
            else:
                max_length = max(max_length, ind - seq_start)
            
            char_dict[char] = ind
        
        return max_length