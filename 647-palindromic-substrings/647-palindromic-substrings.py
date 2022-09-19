class Solution:
    def countSubstrings(self, s: str) -> int:
        
        n = len(s)
        cache = [[False for _ in range(n+1)] for _ in range(n+1)]
        ans = 0

        for g in range(n):
            row, col = 0, g
            while col < n:
                
                if g == 0: cache[row][col] = 1
                elif g == 1 and s[row] == s[col]: cache[row][col] = 1
                else: 
                    if s[row] == s[col] and cache[row+1][col-1]: cache[row][col] = True
                
                if cache[row][col]: ans += 1
                
                row += 1
                col += 1
                
                
                
        return ans