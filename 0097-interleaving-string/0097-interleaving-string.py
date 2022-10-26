class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        m, n, o = len(s1), len(s2), len(s3)
        if n + m != o: return False
        cache = [[False for _ in range(n + 1)] for _ in range(m + 1)]
        cache[m][n] = True

                    
                    
        for i in range(m, -1, -1):
            for j in range(n, -1, -1):
                
                if i < m and s1[i] == s3[i+j] and cache[i+1][j]:
                    cache[i][j] = True
                if j < n and s2[j] == s3[i+j] and cache[i][j+1]:
                    cache[i][j] = True

            

        return cache[0][0]
            