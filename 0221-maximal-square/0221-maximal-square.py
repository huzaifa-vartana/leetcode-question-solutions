class Solution:
    def maximalSquare(self, grid: List[List[str]]) -> int:
        
        m, n = len(grid), len(grid[0])
        cache = [[0 for _ in range(n)] for _ in range(m)]
        maxi = 0
        for j in range(n):
            cache[m-1][j] = int(grid[m-1][j])
            maxi = max(maxi, cache[m-1][j])
        for i in range(m):
            cache[i][n-1] = int(grid[i][n-1])
            maxi = max(maxi, cache[i][n-1])
        
        for i in range(m-2, -1, -1):
            for j in range(n-2, -1, -1):
                
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