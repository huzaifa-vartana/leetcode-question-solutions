class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        # if idx1 >= n: return 1 if idx2 >= m else 0
        # if cache[idx1][idx2] != -1: return cache[idx1][idx2]
        
        n, m = len(s), len(t)
        cache = [[0 for _ in range(m+1)] for _ in range(n+1)]
        for row in range(n+1): cache[row][m] = 1
        for idx1 in range(n-1, -1, -1):
            for idx2 in range(m-1, -1, -1):
                a = 0
                if idx1 < n and idx2 < m and s[idx1] == t[idx2]: a = cache[idx1+1][idx2+1]

                cache[idx1][idx2] = a + cache[idx1+1][idx2]
            
        return cache[0][0]
        