class Solution:
    def countSubstrings(self, s: str) -> int:
        
        n = len(s)
        
        cache = [[0 for _ in range(n+1)] for _ in range(n+1)]
        
        ans = 0
        for g in range(n):
            i, j = 0, g
            while j < n:
                
                if g == 0: cache[i][j] = True
                elif g == 1 and s[i] == s[j]: cache[i][j] = True
                else:
                    if s[i] == s[j] and cache[i+1][j-1]: 
                        cache[i][j] = True
                        
                    
                
                
                if cache[i][j]: ans += 1
                i, j = i+1, j+1
        
        return ans