class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        
        n = len(s)
        cache = [[0 for _ in range(n+1)] for _ in range(n+1)]
        lps = 0
        
        for gap in range(0, n):
            i, j = 0, gap
            while j < n:
                if gap == 0:
                    cache[i][j] = 1
                elif gap == 1:
                    cache[i][j] = 2 if s[i] == s[j] else 1
                else:
                    if s[i] == s[j]:
                        cache[i][j] = 2 + cache[i+1][j-1]
                    else:
                        cache[i][j] = max(cache[i+1][j], cache[i][j-1])
                lps = max(lps, cache[i][j])
                
                j += 1
                i += 1
                
                
                
                
                
        return lps
        