class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        colsum = [0] * len(matrix)
        for row in matrix:
            if len(set(row)) != len(matrix):
                return False
            for ind, val in enumerate(row):
                colsum[ind] += val
        
        if len(set(colsum)) != 1:
            return False
        
        return True
