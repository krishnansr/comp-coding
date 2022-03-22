class Solution:
    def reverseVowels(self, s: str) -> str:
        t = list(s)
        vowels = 'aeiouAEIOU'
        
        i, j = 0, len(t) - 1
        while i < j:
            while i < j and t[i] not in vowels:
                i += 1
            while i < j and t[j] not in vowels:
                j -= 1
                
            t[i], t[j] = t[j], t[i]
            i += 1
            j -= 1
            
        return ''.join(t)