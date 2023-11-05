class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        num_rows = len(matrix)
        num_cols = len(matrix[0])

        # Binary search on the matrix by assuming it’s an array.
        l, r = 0, num_rows * num_cols - 1
        
        while l <= r:
            mid = (l + r) // 2
            row, col = divmod(mid, num_cols)
            if matrix[row][col] < target:
                l = mid + 1
            elif matrix[row][col] >  target:
                r = mid - 1
            else:  # Exact match.
                return True
        
        return False

        
    def searchMatrix_sep(self, matrix: List[List[int]], target: int) -> bool:

        num_rows = len(matrix)
        num_cols = len(matrix[0])

        # Search which row might contain the value.
        l, r = 0, num_rows - 1
        while l <= r:
            mid = (l + r) // 2
            if matrix[mid][-1] < target:
                l = mid + 1
            elif matrix[mid][-1] >  target:
                r = mid - 1
            else:  # Exact match.
                return True
        
        row = min(l, num_rows - 1)

        l, r = 0, num_cols - 1
        while l <= r:
            mid = (l + r) // 2
            if matrix[row][mid] < target:
                l = mid + 1
            elif matrix[row][mid] > target:
                r = mid - 1
            else:  # Exact match.
                return True

        return False
