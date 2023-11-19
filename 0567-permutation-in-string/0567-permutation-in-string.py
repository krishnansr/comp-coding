class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        
        s1_map = dict()
        for char in s1:
            s1_map[char] = s1_map.get(char, 0) + 1
        
        s2_map = dict()
        l, r = 0, 0
        while r < len(s2):
            if s1_map == s2_map:
                return True
            
            if r - l == len(s1):
                # Recieved enough characters since (r - l) == len(s1
                # so keep moving l up to maintain window size.
                s2_map[s2[l]] -= 1
                if s2_map[s2[l]] == 0:
                    s2_map.pop(s2[l])
                l += 1
            # Keep adding r to s2_map everytime.
            s2_map[s2[r]] = s2_map.get(s2[r], 0) + 1
            r += 1
        
        return s1_map == s2_map
    
    def checkInclusion_old(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        
        s1_map = dict()
        for char in s1:
            s1_map[char] = s1_map.get(char, 0) + 1
        
        s2_map = dict()
        l, r = 0, 0
        while r < len(s2):
            if s2[r] not in s1_map:
                # saw irrelevant char
                if l < r:
                    # check if the maps are equal.
                    if s1_map == s2_map:
                        return True

                    # keep shrinking the window.
                    if s2_map[s2[l]] > 1:
                        s2_map[s2[l]] -= 1
                    else:
                        s2_map.pop(s2[l])
                    l += 1
                else:
                    # keep moving to next char
                    l += 1
                    r += 1
                    continue
            else:
                # keep expanding the window.
                s2_map[s2[r]] = s2_map.get(s2[r], 0) + 1
                r += 1
        return s1_map == s2_map