class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        frog_map = {'c': 0, 'r': 1, 'o': 2, 'a':3, 'k': 4}
        frog_list = [0] * 5
        
        curr_frogs, max_frogs = 0, 0
        
        for ch in croakOfFrogs:
            ch_ind = frog_map[ch]
            frog_list[ch_ind] += 1
        
            if ch_ind > 0:
                frog_list[ch_ind - 1] -= 1
                if frog_list[ch_ind - 1] < 0:
                    return -1  # invalid seq of chars
            
            if ch_ind == 0:  # first character of 'croak'
                curr_frogs += 1
                max_frogs = max(max_frogs, curr_frogs)
            elif ch_ind == len(frog_list) - 1:  # last character of 'croak'
                curr_frogs -= 1
        
        return max_frogs if any(frog_list[:-1]) == False else -1