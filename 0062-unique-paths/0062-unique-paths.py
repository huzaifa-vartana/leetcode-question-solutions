class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        def valid(x, y): return x >= 0 and x < m and y >= 0 and y < n
        cache = [[-1 for _ in range(n + 1)] for _ in range(m + 1)]
        
        def solve(i, j):
            if i == m - 1 and j == n - 1: return 1
            if cache[i][j] != -1: return cache[i][j]
            
            count = 0
            for nr, nc in [(i+1, j), (i, j+1)]:
                if not valid(nr, nc): continue
                count += solve(nr, nc)
                
            cache[i][j] = count
            return cache[i][j]
            
            
        return solve(0, 0)