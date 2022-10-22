class Solution:
	moves = [(-1, 0), (0, -1), (1, 0), (0, 1)]

	def pacificAtlantic(self, heights: List[List[int]]) -> Set[Tuple[int, int]]:
		r, c = len(heights), len(heights[0])
		atl_visited = set()
		pas_visited = set()

		def dfs(i: int, j: int, visited: set):
			visited.add((i, j))
			for di, dj in self.moves:
				x, y = i + di, j + dj
				if 0 <= x < r and 0 <= y < c and (x, y) not in visited and heights[i][j] <= heights[x][y]:
					dfs(x, y, visited)

		for i in range(r):
			dfs(i,     0, pas_visited)
			dfs(i, c - 1, atl_visited)

		for j in range(c):
			dfs(    0, j, pas_visited)
			dfs(r - 1, j, atl_visited)

		return atl_visited & pas_visited