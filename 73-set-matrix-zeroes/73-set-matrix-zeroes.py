class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m = len(matrix)
        n = len(matrix[0])
        is_first_row_zero = False
        is_first_col_zero = False

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    if i == 0:
                        is_first_row_zero = True
                    if j == 0:
                        is_first_col_zero = True
                    matrix[i][0] = matrix[0][j] = 0
                    
        for i in range(m):
            for j in range(n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
                    
        if is_first_row_zero:
            matrix[0][:] = [0] * n
            
        if is_first_col_zero:
            for i in range(m):
                matrix[i][0] = 0
        
        
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        i_inds = set()
        j_inds = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    i_inds.add(i)
                    j_inds.add(j)
                    
        for i in range(len(matrix)):
            if i in i_inds:
                matrix[i][:] = [0] * len(matrix[0])
                continue
            for j in range(len(matrix[0])):
                if j in j_inds:
                    matrix[i][j] = 0