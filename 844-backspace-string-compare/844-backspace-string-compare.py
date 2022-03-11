class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_mod = ''
        for _char in s:
            if _char == '#':
                s_mod = s_mod[:-1]
            else:
                s_mod += _char
                
        t_mod = ''
        for _char in t:
            if _char == '#':
                t_mod = t_mod[:-1]
            else:
                t_mod += _char
                
        return s_mod == t_mod