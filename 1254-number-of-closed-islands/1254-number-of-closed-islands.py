class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        
        m, n = len(grid), len(grid[0])
        cache = [[0 for _ in range(n+ 1)] for _ in range(m + 1)]
        def valid(x, y): return x >= 0 and x < m and y >= 0 and y < n

        
        def solve(i, j):
            
            grid[i][j] = 1
            for nr, nc in [(i, j+1), (i+1, j), (i-1, j), (i, j-1)]:
                if not valid(nr, nc) or grid[nr][nc] == 1: continue
                solve(nr, nc)
                
            
        for i in range(m):
            for j in range(n):
                if (i * j == 0 or i == m - 1 or j == n - 1) and grid[i][j] == 0:
                    solve(i, j)
         

        count = 0            
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0: 
                    solve(i, j)
                    count += 1
                    
        return count