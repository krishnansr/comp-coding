class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # solution to https://leetcode.com/problems/flood-fill
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
    
    def numIslands(self, grid: List[List[str]]) -> int:
        island_count = 0
        
        for sr in range(len(grid)):
            for sc in range(len(grid[0])):
                if grid[sr][sc] == "1":
                    grid = self.floodFill(grid, sr, sc, "2")  # seen island
                    island_count += 1
        
        return island_count