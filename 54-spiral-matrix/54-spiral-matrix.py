class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if matrix:
            first_row = matrix.pop(0)
            return first_row + self.spiralOrder([list(x) for x in zip(*matrix)][::-1])
        return []
