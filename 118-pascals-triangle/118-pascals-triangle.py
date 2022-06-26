class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1], [1, 1]]
        for n in range(1, numRows - 1):
            new_row = [res[-1][i] + res[-1][i + 1] for i in range(n)]
            res.append([1, *new_row, 1])
               
        return res[:numRows]