class Solution:
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