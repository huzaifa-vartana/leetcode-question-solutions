class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        
        
        
        cuts.append(0)
        cuts.append(n)
        c = len(cuts)
        cuts.sort()
        
        @lru_cache(None)
        def solve(i, j):
            
            if i > j: return 0
            mini = float('inf')
            for k in range(i, j+1):
                mini = min(
                    mini,
                    solve(i, k-1) + solve(k+1, j) + cuts[j+1] - cuts[i-1]
                )
                
            return mini
            
            
        return solve(1, c-2)