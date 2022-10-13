class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        
        # cache = [[-1 for _ in range(n+1)] for _ in range(n+1)]
        @lru_cache(None)
        def solve(i, j):

            if i >= j: return 0
            # if cache[i][j] != -1: return cache[i][j] 

            mini = float('inf')
            cut_poss = False
            for cut in cuts:
                if i < cut < j:
                    cut_poss = True
                    mini = min(solve(i, cut) + solve(cut, j) + j - i, mini)
            
            # cache[i][j] = mini if cut_poss else 0
            # return cache[i][j]
            return mini if cut_poss else 0
        
        
        return solve(0, n)
        