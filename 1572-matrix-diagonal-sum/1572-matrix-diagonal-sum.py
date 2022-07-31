class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        return sum(row[i] + row[-1 - i]  for i, row in enumerate(mat))  - (1 & len(mat)) * mat[len(mat) // 2][len(mat) // 2]