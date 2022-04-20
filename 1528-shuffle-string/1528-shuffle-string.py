class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        return ''.join([_char for _, _char in sorted(zip(indices, s))])