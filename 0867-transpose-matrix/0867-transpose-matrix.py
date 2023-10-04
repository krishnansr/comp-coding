class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        return zip(*matrix)
        
    def transpose_iter(self, matrix: List[List[int]]) -> List[List[int]]:
        trans = [[] for _ in range(len(matrix[0]))]
        for row in matrix:
            for i in range(len(row)):
                trans[i].append(row[i])
        return trans
        
    def transpose_square(self, matrix: List[List[int]]) -> List[List[int]]:
        for r in range(len(matrix)):
            for c in range(r + 1, len(matrix[0])):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
        return matrix