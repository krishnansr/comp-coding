class Solution:
    def convertToTitle(self, num: int) -> str:
        title = ''
        while num > 0:
            num -= 1
            title = chr(num % 26 + 65) + title
            num = num // 26
            
        return title

