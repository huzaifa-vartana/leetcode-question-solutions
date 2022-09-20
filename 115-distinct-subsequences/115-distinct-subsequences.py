class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        
        n, m = len(s), len(t)
        cache = [[-1 for _ in range(m+1)] for _ in range(n+1)]
        def solve(idx1, idx2):
            
            if idx1 >= n: return 1 if idx2 >= m else 0
            if cache[idx1][idx2] != -1: return cache[idx1][idx2]
            
            a = 0
            if idx1 < n and idx2 < m and s[idx1] == t[idx2]: a = solve(idx1+1, idx2+1)
            
            cache[idx1][idx2] = a + solve(idx1+1, idx2)
            return cache[idx1][idx2] 
            
        return solve(0, 0)
        