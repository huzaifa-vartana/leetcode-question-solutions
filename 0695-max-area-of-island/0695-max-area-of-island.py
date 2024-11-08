class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        N, M = len(grid), len(grid[0])
        def valid(x, y): return x >= 0 and x < N and y >= 0 and y < M
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        def dfs(i, j):
            
            grid[i][j] = 0
            count = 1
            for r, c in directions:
                i_, j_ = i + r, j + c
                if not valid(i_, j_): continue
                if grid[i_][j_] == 0: continue
                count += dfs(i_, j_)

            return count

        max_area = 0
        for i in range(N):
            for j in range(M):
                if grid[i][j] == 1:
                    max_area = max(max_area, dfs(i, j))
        return max_area


        
