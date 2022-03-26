class Solution:
    _ascii = set(string.ascii_lowercase)
    
    def reverseOnlyLetters(self, s: str) -> str:
        str_s = list(s)
        i, j = 0, len(s) - 1
        while i < j:
            while i < j and str_s[i].lower() not in self._ascii:
                i += 1
            while i < j and str_s[j].lower() not in self._ascii:
                j -= 1
            
            str_s[i], str_s[j] = str_s[j], str_s[i]
            i += 1
            j -= 1
        
        return ''.join(str_s)