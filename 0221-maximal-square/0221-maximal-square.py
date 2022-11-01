class Solution:
    def maximalSquare(self, grid: List[List[str]]) -> int:
        
        m, n = len(grid), len(grid[0])
        cache = [[-1 for _ in range(n+1)] for _ in range(m+1)]
        # for j in range(n):
        #     cache[m-1][j] = int(grid[m-1][j])
        # for i in range(m):
        #     cache[i][n-1] = int(grid[i][n-1])
        def valid(x, y): return x >= 0 and x < m and y >= 0 and y < n
        
        maxi = 0
        def solve(i, j):
            if not valid(i, j): return 0
            if cache[i][j] != -1: return cache[i][j]

            d = solve(i+1, j)
            r = solve(i, j+1)
            dig = solve(i+1, j+1)

            if grid[i][j] == '1':
                ans = 1 + min(r, d, dig)
                nonlocal maxi
                maxi = max(maxi, ans)
                cache[i][j] = ans
                return ans
            else:
                cache[i][j] = 0
                return 0
            
        solve(0, 0)
        return maxi ** 2