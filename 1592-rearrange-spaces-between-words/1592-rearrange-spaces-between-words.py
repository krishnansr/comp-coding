class Solution:
    def reorderSpaces(self, text: str) -> str:
        words = text.split()
        a, b = len(text) - sum(map(len, words)), (len(words) - 1)
        if b:
            spaces, trail = a // b, a % b
        else:
            spaces, trail = 0, a
        return (' ' * spaces).join(words) + ' ' * trail