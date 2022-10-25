class Solution:
    def longestCommonSubsequence(self, t1: str, t2: str) -> int:
        
        m, n = len(t1), len(t2)
        cache = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
            
                if t1[i] == t2[j]: cache[i][j] = 1 + cache[i+1][j+1]
                else: cache[i][j] = max(cache[i][j+1], cache[i+1][j])

        
        

        return cache[0][0]
        