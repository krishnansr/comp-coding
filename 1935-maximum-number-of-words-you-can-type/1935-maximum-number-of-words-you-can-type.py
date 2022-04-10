class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        count = 0
        carry = 1
        for _char in text:
            if _char == ' ':
                if carry:
                    count += 1
                carry = 1
            elif not carry:
                continue
            elif _char in brokenLetters:
                carry = 0
        
        return count + carry