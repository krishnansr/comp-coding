class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        for _char in s[::-1]:
            if _char == ' ':
                if count:
                    return count
                else:
                    continue
            count += 1
        
        return count