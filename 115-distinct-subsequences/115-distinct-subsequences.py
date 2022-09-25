class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        n, m = len(s), len(t)
        
        
        cache = [[-1 for _ in range(m+1)] for _ in range(n+1)]
        def solve(i, j):
            
            if j >= m: return 1
            if i >= n: return 0
            if i >= n: return 1 if j >= m else 0
            if cache[i][j] != -1: return cache[i][j]
            
            count = 0
            if s[i] == t[j]:
                count += solve(i+1, j+1)
                
            cache[i][j] = count + solve(i+1, j)
            return cache[i][j] 
        
        
        return solve(0, 0)
        
        
        