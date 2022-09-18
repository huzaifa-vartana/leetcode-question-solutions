class Solution:
    def longestCommonSubsequence(self, s: str, t: str) -> int:
        
        
        l1, l2 = len(s), len(t)
        cache = [[0 for _ in range(l2+1)] for _ in range(l1+1)]
        for i in range(l1-1, -1, -1):
            for j in range(l2-1, -1, -1):
                
                match = 0
                if s[i] == t[j]: match = 1 + cache[i+1][j+1]
            
                cache[i][j] = max(cache[i+1][j], cache[i][j+1], match)
            

        return cache[0][0]
            