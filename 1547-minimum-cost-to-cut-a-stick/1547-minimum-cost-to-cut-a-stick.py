class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        
        cuts.append(0)
        cuts.append(n)
        cuts.sort()
        c = len(cuts)
        cache = [[-1 for _ in range(c+1)] for _ in range(c+1)]
        
        def solve(i, j):
            
            if i > j: return 0
            if cache[i][j] != -1: return cache[i][j]
            
            mini = float('inf')
            for cut in range(i, j+1):
                mini = min(
                    mini,
                    solve(i, cut-1) + solve(cut+1, j) + cuts[j+1] - cuts[i-1]
                )
            cache[i][j] = mini
            return cache[i][j] 
            
            
        return solve(1, c-2)