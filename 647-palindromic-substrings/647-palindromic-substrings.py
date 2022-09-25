class Solution:
    def countSubstrings(self, s: str) -> int:
        
        n, count = len(s), 0
        cache = [[False for _ in range(n+1)] for _ in range(n+1)]
        
        for gap in range(n):
            i, j = 0, gap
            while j < n:
                
                if gap == 0: cache[i][j] = True
                elif gap == 1 and s[i] == s[j]: cache[i][j] = True
                else:
                    if s[i] == s[j] and cache[i+1][j-1]: cache[i][j] = True
                
                if cache[i][j]: count += 1
                i += 1
                j += 1
                
                
        return count