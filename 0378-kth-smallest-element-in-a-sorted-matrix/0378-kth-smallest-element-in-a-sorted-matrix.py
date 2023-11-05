class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        # if you use max-heap (like in kth smallest element question) then 
        # you're not leveraging the inherent sorted order statistic from the matrix
        # instead use this min-heap solution from https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/discuss/1322101/C++JavaPython-MaxHeap-MinHeap-Binary-Search-Picture-Explain-Clean-and-Concise
        
        # O(klogk) time, O(k) space.
        num_rows = len(matrix)
        num_cols = len(matrix[0])
        
        # initialize min-heap to first column, store (value, r, c)
        heap = [(matrix[r][0], r, 0) for r in range(min(k, num_rows))]  # already sorted.
        
        ans = -1
        for i in range(k):
            ans, r, c = heapq.heappop(heap)  # ans is the i_th smallest value.
            if c + 1 < num_cols:  # i. e. if next column is a valid col index.
                heapq.heappush(heap, (matrix[r][c + 1], r, c + 1))
        return ans