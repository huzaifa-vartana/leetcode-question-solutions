class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:

        N, M = 2, len(grid[0])
        top_sum = sum(grid[0])
        bottom_sum = 0
        ans = float('inf')

        for idx in range(len(grid[0])):
            top_sum -= grid[0][idx]
            ans = min(ans, max(top_sum, bottom_sum))
            bottom_sum += grid[1][idx]

        return ans
            