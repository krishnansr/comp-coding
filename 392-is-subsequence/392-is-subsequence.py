class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_ptr, t_ptr = 0, 0
        while t_ptr < len(t) and s_ptr < len(s):
            if t[t_ptr] == s[s_ptr]:
                s_ptr += 1
            t_ptr += 1
        return s_ptr == len(s)