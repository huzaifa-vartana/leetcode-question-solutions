class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        count = 0
        N, M = len(grid), len(grid[0])
        def helper(i, j):
            if i < 0 or i >= N or j < 0 or j >= M: return True
            if grid[i][j] == "0": return True

            grid[i][j] = "0"
            helper(i+1, j)
            helper(i, j+1)
            helper(i-1, j)
            helper(i, j-1)

        for i in range(N):
            for j in range(M):
                if grid[i][j] == "1":
                    helper(i, j)
                    count += 1
        return count