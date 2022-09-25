class Solution:
    def minDistance(self, s: str, t: str) -> int:
        
        
        
        n, m = len(s), len(t)
        cache = [[-1 for _ in range(m+1)] for _ in range(n+1)]
        def cache1(i, j):
            
            if i >= n and j >= m: return 0
            if i >= n: return m - j
            if j >= m: return n - i
            if cache[i][j] != -1: return cache[i][j]
            
            
            
            if s[i] != t[j]:
                cache[i][j] = 1 + min(cache1(i+1, j+1), cache1(i, j+1), cache1(i+1, j))
                return cache[i][j]
            
            cache[i][j] = cache1(i+1, j+1)
            return cache[i][j]
            
                
        return cache1(0, 0)
        
        
        