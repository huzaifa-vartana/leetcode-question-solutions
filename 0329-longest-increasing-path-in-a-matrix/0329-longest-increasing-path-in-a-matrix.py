class Solution:
    def longestIncreasingPath(self, grid: List[List[int]]) -> int:
        
        
        m, n = len(grid), len(grid[0])
        def valid(x, y): return x >= 0 and x < m and y >= 0 and y < n
        cache = [[-1 for _ in range(n     + 1)] for _ in range(m + 1)]
        
        def solve(i, j):
            if cache[i][j] != -1: return cache[i][j]
            
            longi = 0
            for nr, nc in [(i, j+1), (i+1, j), (i-1, j), (i, j-1)]:
                if not valid(nr, nc): continue
                if grid[i][j] >= grid[nr][nc]: continue
                longi = max(
                    longi,
                    1 + solve(nr, nc)
                )
              
            cache[i][j] = longi
            return longi
        
        
        longi = 0
        for i in range(m):
            for j in range(n):
                longi = max(
                    longi,
                    solve(i, j) + 1
                )
                
        return longi