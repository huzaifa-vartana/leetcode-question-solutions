class Solution:
    def maximalSquare(self, grid: List[List[str]]) -> int:
        
        m, n = len(grid), len(grid[0])
        cache = [[0 for _ in range(n+1)] for _ in range(m+1)]
        def valid(x, y): return x >= 0 and x < m and y >= 0 and y < n
        
        maxi = 0
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                
                d = cache[i+1][j]
                r = cache[i][j+1]
                dig = cache[i+1][j+1]

                if grid[i][j] == '1':
                    ans = 1 + min(r, d, dig)
                    maxi = max(maxi, ans)
                    cache[i][j] = ans
                else:
                    cache[i][j] = 0
            
        
        return maxi ** 2