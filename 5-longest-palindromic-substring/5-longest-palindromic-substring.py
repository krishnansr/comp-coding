class Solution:
    def longestPalindrome(self, s: str) -> str:
        start = -1
        res_len = -1
        
        for i in range(len(s)):
            
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l> res_len:
                    start = l
                    res_len = r - l
                l -= 1
                r += 1
                
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l > res_len:
                    start = l
                    res_len = r - l
                l -= 1
                r += 1
            
        return s[start: start + res_len + 1]