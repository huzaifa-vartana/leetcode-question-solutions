class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:

        N, M = len(grid), len(grid[0])
        seen = set()
        def dfs(i, j):
            if (i, j) in seen: return 0
            if i < 0 or i >= N or j < 0 or j >= M: return 1
            if grid[i][j] == 0: return 1

            seen.add((i, j))
            c1 = dfs(i+1, j)
            c2 = dfs(i-1, j) 
            c3 = dfs(i, j-1) 
            c4 = dfs(i, j+1) 
            return c1 + c2 + c3 + c4
        
        
        for i in range(N):
            for j in range(M):
                if grid[i][j] == 1: return dfs(i, j)
