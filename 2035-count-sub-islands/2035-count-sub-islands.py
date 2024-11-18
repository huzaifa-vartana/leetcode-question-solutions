class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        N, M = len(grid1), len(grid1[0])
        ctr = 0
        def valid(x, y): return x >= 0 and x < N and y >= 0 and y < M
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        def dfs(i, j):
            grid2[i][j] = 0
            match = grid1[i][j] == 1
            for x, y in directions:
                i_, j_ = i + x, j + y
                if not valid(i_, j_) or grid2[i_][j_] == 0: continue
                if not dfs(i_, j_): 
                    match = False  # Update match only if any recursive call is False
            return match
        
        for i in range(N):
            for j in range(M):
                if grid1[i][j] == 1 and grid2[i][j] == 1 and dfs(i, j): ctr += 1
        return ctr
  