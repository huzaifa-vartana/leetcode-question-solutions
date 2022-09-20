class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        
        
#         left, right
# lcs
# gap method
        n = len(s)
        cache = [[0 for _ in range(n+1)] for _ in range(n+1)]
        ans = 0
        for g in range(n):
            i, j = 0, g
            
            while j < n:
                if g == 0:
                    cache[i][j] = 1
                elif g == 1:
                    cache[i][j] = 2 if s[i] == s[j] else 1
                else:
                    if s[i] == s[j]:
                        cache[i][j] = 2 + cache[i+1][j-1]
                    else:
                        cache[i][j] = max(cache[i+1][j], cache[i][j-1])
                        
                ans = max(ans, cache[i][j])
                
                
                
                
                i += 1
                j += 1
        
        return ans