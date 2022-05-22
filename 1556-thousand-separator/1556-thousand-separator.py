class Solution:
    def thousandSeparator(self, n: int) -> str:
        ls = str(n)[::-1]
        return '.'.join([ls[i: i+3] for i in range(0, len(ls), 3)])[::-1]
            