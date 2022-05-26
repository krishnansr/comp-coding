class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        i, j = len(s) - 1, len(t) - 1
        del_i, del_j = 0, 0
        
        while i > -1 or j > -1:
            if i > -1  and (s[i] == '#' or del_i):
                del_i += 1 if s[i] == '#' else -1
                i -= 1
                continue

            if j > -1 and (t[j] == '#' or del_j):
                del_j += 1 if t[j] == '#' else -1
                j -= 1
                continue

            if s[i] != t[j]:
                return False
            
            i -= 1
            j -= 1
        return i == j
