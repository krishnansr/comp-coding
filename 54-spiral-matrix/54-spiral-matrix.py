class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # sol: https://leetcode.com/problems/spiral-matrix/discuss/20571/1-liner-in-Python-%2B-Ruby
        if matrix:
            first_row = matrix.pop(0)
            return first_row + self.spiralOrder([list(x) for x in zip(*matrix)][::-1])
        return []
