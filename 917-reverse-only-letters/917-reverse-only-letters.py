class Solution:
    
    def reverseOnlyLetters(self, s: str) -> str:
        str_s = list(s)
        i, j = 0, len(s) - 1
        while i < j:
            while i < j and not str_s[i].isalpha():
                i += 1
            while i < j and not str_s[j].isalpha():
                j -= 1
            str_s[i], str_s[j] = str_s[j], str_s[i]
            i += 1
            j -= 1
        
        return ''.join(str_s)