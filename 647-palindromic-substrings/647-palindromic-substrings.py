class Solution:
    def countSubstrings(self, s: str) -> int:
        
        
        n, count = len(s), 0
        cache = [[False for _ in range(n+1)] for _ in range(n+1)]
        
        for gap in range(n):
            row, col = 0, gap
            while col < n:
                
                if gap == 0: cache[row][col] = True
                elif gap == 1: cache[row][col] = s[row] == s[col]
                else:
                    if s[row] == s[col] and cache[row+1][col-1]: cache[row][col] = True
                
                if cache[row][col]: count += 1
                row += 1
                col += 1
                
                
        return count