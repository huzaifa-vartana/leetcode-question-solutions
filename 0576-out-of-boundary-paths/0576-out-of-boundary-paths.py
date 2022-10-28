class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        
        
        MOD = 10 ** 9 + 7

        # cache = [[0 for _ in range(n+ 1)] for _ in range(m + 1)]
        def valid(x, y): return x >= 0 and x < m and y >= 0 and y < n

        @lru_cache(None)
        def solve(i, j, moves):
            if not valid(i, j): return 1
            if moves >= maxMove: return 0
            
            count = 0
            for nr, nc in [(i, j+1), (i+1, j), (i-1, j), (i, j-1)]:
                count += solve(nr, nc, moves + 1)
            
            
            return count % MOD
            
            
        return solve(startRow, startColumn, 0)