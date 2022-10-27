class Solution:
    def minDistance(self, w1: str, w2: str) -> int:
        
        m, n = len(w1), len(w2)
        
        @lru_cache(None)
        def solve(i, j):
            
            if i >= m:
                return n - j
            if j >= n:
                return m - i
            if w1[i] == w2[j]: return solve(i+1, j+1)
            
            # insert
            ins = 1 + solve(i, j+1)
            # delete
            d = 1 + solve(i+1, j)
            # replace
            r = 1 + solve(i+1, j+1)
            
            return min(ins, d, r)
        
        return solve(0, 0)