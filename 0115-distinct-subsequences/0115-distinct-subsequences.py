class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        
        m, n = len(s), len(t)
        
        @lru_cache(None)
        def solve(i, j):
            
            if i >= m:
                return 1 if j >= n else 0
            
            count = 0
            if i < m and j < n and s[i] == t[j]:
                count += solve(i+1, j+1)
            
            return solve(i+1, j) + count
        
        return solve(0, 0)