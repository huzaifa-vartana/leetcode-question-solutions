class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        
        MOD = 10 ** 9 + 7
        def valid(x, y):
            return x >= 0 and x < m and y >= 0 and y < n


        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]


        @lru_cache(None)
        def solve(i, j, moves):

            if not valid(i, j): return 1
            if moves <= 0: return 0

            count = 0
            for dx, dy in directions:
                nr, nc = dx + i, dy + j
                count += solve(nr, nc, moves - 1)

            return count % MOD


        return solve(startRow, startColumn, maxMove)