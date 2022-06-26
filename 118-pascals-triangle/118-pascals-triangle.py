class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1], [1, 1]]
        for n in range(1, numRows - 1):
            res.append([1] + [res[-1][i] + res[-1][i + 1] for i in range(n)] + [1])
               
        return res[:numRows]