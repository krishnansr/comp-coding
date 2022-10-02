class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        src_color = image[sr][sc]
        if src_color == color:
            return image
        
        def dfs(row, col):
            if 0 <= row < len(image) and 0 <= col < len(image[0]) and image[row][col] == src_color:
                image[row][col] = color
                
                dfs(row, col - 1)
                dfs(row, col + 1)
                dfs(row - 1, col)
                dfs(row + 1, col)
        
        dfs(sr, sc)
        return image