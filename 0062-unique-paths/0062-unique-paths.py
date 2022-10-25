class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        def valid(x, y): return x >= 0 and x < m and y >= 0 and y < n
        cache = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        cache[m-1][n-1] = 1

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if i == m - 1 and j == n - 1: continue
    
                count = 0
                for nr, nc in [(i+1, j), (i, j+1)]:
                    if not valid(nr, nc): continue
                    count += cache[nr][nc]

                cache[i][j] = count

            
            
        return cache[0][0]