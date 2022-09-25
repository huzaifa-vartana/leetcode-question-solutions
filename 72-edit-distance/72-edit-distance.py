class Solution:
    def minDistance(self, s: str, t: str) -> int:
        
        
        
        n, m = len(s), len(t)
        cache = [[0 for _ in range(m+1)] for _ in range(n+1)]
        for col in range(m+1):
            cache[n][col] = m - col
        for row in range(n+1):
            cache[row][m] = n - row
            
        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):
                
                if s[i] != t[j]: cache[i][j] = 1 + min(cache[i+1][j+1], cache[i][j+1], cache[i+1][j])
                else: cache[i][j] = cache[i+1][j+1]

            
        return cache[0][0]
        
        
        