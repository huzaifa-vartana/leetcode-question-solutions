class Solution:
    def longestCommonSubsequence(self, t1: str, t2: str) -> int:
        
        m, n = len(t1), len(t2)
        cache = [[-1 for _ in range(n + 1)] for _ in range(m + 1)]
        
        def solve(i, j):
            if i >= m or j >= n: return 0
            if cache[i][j] != -1: return cache[i][j]
            
            if t1[i] == t2[j]:
                cache[i][j] = 1 + solve(i+1, j+1)
                return cache[i][j]
            cache[i][j] = max(solve(i+1, j), solve(i, j+1))
            return cache[i][j]
        
        

        return solve(0, 0)
        