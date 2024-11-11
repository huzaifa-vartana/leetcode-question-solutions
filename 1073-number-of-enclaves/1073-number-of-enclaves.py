class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        N, M = len(grid), len(grid[0])
        def valid(x, y): return x >= 0 and x < N and y >= 0 and y < M

        seen = set()
        def dfs(i, j, seen):
            if seen is not None: seen.add((i, j))
            grid[i][j] = 0
            for i_, j_ in [(i, j+1), (i+1, j), (i-1, j), (i, j-1)]:
                if not valid(i_, j_) or grid[i_][j_] == 0: continue
                dfs(i_, j_, seen)

        for i in range(N):
            for j in range(M):
                if i == 0 or i == N - 1 or j == 0 or j == M - 1: 
                    if grid[i][j] == 1: dfs(i, j, None)

        for i in range(N):
            for j in range(M):
                if grid[i][j] == 1: dfs(i, j, seen)


        return len(seen)