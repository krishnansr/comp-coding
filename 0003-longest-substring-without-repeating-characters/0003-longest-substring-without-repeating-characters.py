class Solution:
    def lengthOfLongestSubstring(self, string: str) -> int:
        char_set = set()
        max_length = 0
        
        l, r = 0, 0
        while r < len(string):
            
            if string[r] not in char_set:
                char_set.add(string[r])
                r += 1
                max_length = max(max_length, r - l)
            else:
                # Char is in set, need to remove it before expanding sliding window.
                char_set.remove(string[l])
                l += 1
            
        return max_length