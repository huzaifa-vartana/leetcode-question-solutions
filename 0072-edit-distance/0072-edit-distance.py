class Solution:
    def minDistance(self, s: str, t: str) -> int:
        
        m, n = len(s), len(t)
        
        cache = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for j in range(n+1):
            cache[m][j] = n - j
        for i in range(m+1):
            cache[i][n] = m - i
                    
        # n, m = len(s), len(t)    
        # for col in range(m+1):
        #     cache[n][col] = m - col
        # for row in range(n+1):
        #     cache[row][m] = n - row
            
        
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                
                if s[i] != t[j]: cache[i][j] = 1 + min(cache[i+1][j+1], cache[i][j+1], cache[i+1][j])
                else: cache[i][j] = cache[i+1][j+1]
                    
        return cache[0][0]