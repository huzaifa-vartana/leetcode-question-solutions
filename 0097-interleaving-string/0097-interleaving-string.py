class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        m, n, o = len(s1), len(s2), len(s3)
        
        cache = [[-1 for _ in range(n+ 1)] for _ in range(m + 1)]
        def solve(i, j, k):
            if k >= o: 
                return True if i >= m and j >= n else False
            if i >= m and j >= n: return False
            if cache[i][j] != -1: return cache[i][j]
            
            
            if i < m and s1[i] == s3[k] and solve(i+1, j, k+1):
                return True
            if j < n and s2[j] == s3[k] and solve(i, j+1, k+1):
                return True
               
            cache[i][j] = False
            return False
            
        
        return solve(0, 0, 0)
            