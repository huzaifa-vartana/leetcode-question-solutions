class Solution:
    def pacificAtlantic(self, grid: List[List[int]]) -> List[List[int]]:
        N, M = len(grid), len(grid[0])
        atl, pac = set(), set()
        res = []
        def valid(x, y): return x >= 0 and x < N and y >= 0 and y < M
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        def dfs(i, j, visited, prev):
            if not valid(i, j): return
            if grid[i][j] < prev: return
            if (i, j) in visited: return
            
            visited.add((i, j))
            dfs(i+1, j, visited, grid[i][j])
            dfs(i-1, j, visited, grid[i][j])
            dfs(i, j+1, visited, grid[i][j])
            dfs(i, j-1, visited, grid[i][j])

        for j in range(M):
            dfs(0, j, pac, grid[0][j])
            dfs(N-1, j, atl, grid[N-1][j])
        for i in range(N):
            dfs(i, 0, pac, grid[i][0])
            dfs(i, M-1, atl, grid[i][M-1])

        for i in range(N):
            for j in range(M):
                if (i, j) in pac and (i, j) in atl:
                    res.append([i, j])

        return res
        