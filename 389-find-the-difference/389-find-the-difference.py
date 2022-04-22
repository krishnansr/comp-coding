class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        res = 0
        for _char in s  + t:
            res ^= ord(_char)
        return chr(res)
        
        
    def findTheDifference_array(self, s: str, t: str) -> str:
        count = [0] * 26
        for _char in s:
            count[ord(_char) - 97] += 1
        
        for _char in t:
            if not count[ord(_char) - 97]:
                return _char
            count[ord(_char) - 97] -= 1
        
        return ''