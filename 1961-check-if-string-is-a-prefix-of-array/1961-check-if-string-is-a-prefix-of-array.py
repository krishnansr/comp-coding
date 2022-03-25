class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        pos = 0
        for word in words:
            if word == s[pos: pos + len(word)]:
                pos += len(word)
            else:
                return False
            
            if pos == len(s):
                return True
        return False