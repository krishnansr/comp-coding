class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # O(m + n) solution. Trick is to start from top-right corner.
        # explanation in https://leetcode.com/problems/search-a-2d-matrix-ii/discuss/332356/Python-O(m%2Bn)-Linear-Search-from-Top-Right-Corner
        
        num_rows = len(matrix)
        num_cols = len(matrix[0])

        # Start from top-right corner.
        r, c = 0, num_cols - 1
        
        while r < num_rows and c >= 0:
            if matrix[r][c] > target:
                c -= 1
            elif matrix[r][c] < target:
                r += 1
            else:
                return True
        return False
