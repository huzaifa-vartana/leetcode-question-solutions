class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        n, m = len(s), len(t)
        
        
        cache = [[0 for _ in range(m+1)] for _ in range(n+1)]
        for row in range(n+1): cache[row][m] = 1
        
        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):
                
                count = 0
                if s[i] == t[j]: count += cache[i+1][j+1]
                cache[i][j] = count + cache[i+1][j]

        
        
        return cache[0][0]
        
        
        