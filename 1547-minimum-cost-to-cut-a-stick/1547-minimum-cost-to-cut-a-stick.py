class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        
        @lru_cache(None)
        def solve(i, j):


            mini = float('inf')
            cut_poss = False
            for cut in cuts:
                if i < cut < j:
                    cut_poss = True
                    mini = min(solve(i, cut) + solve(cut, j) + j - i, mini)
            
            return mini if cut_poss else 0
        
        
        return solve(0, n)
        