class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        
        @lru_cache(None)
        def solve(i, j):
            
            if i > j: return 0
            mini = float('inf')
            for cut in cuts:
                if i < cut < j:
                    mini = min(
                        mini,
                        solve(i, cut) + solve(cut, j) + j - i
                    )
                
            return 0 if mini == float('inf') else mini
            
            
        return solve(0, n)