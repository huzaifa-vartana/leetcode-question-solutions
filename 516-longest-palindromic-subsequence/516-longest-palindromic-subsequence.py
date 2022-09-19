class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        
        n = len(s)
        cache = [[0 for _ in range(n+1)] for _ in range(n+1)]
        ans = 0
        for gap in range(0, n):
            row, col = 0, gap
            while col < n:
                
                if gap == 0:
                    cache[row][col] = 1
                elif gap == 1:
                    cache[row][col] = 2 if s[row] == s[col] else 1
                else:
                
                    if s[col] == s[row]:
                        cache[row][col] = 2 + cache[row+1][col-1]
                    else:
                        cache[row][col] = max(cache[row][col-1], cache[row+1][col])
                ans = max(ans, cache[row][col]) 
                    
                
                row += 1
                col += 1
             
                
                
        return ans