class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        _str = [''] * len(indices)
        for c, i in zip(s, indices):
            _str[i] = c
        return ''.join(_str)
    
    def restoreString_sorted(self, s: str, indices: List[int]) -> str:
        return ''.join([_char for _, _char in sorted(zip(indices, s))])