class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        
        # cache = [[-1 for _ in range(n+1)] for _ in range(n+1)]
        cuts.append(0)
        cuts.append(n)
        total_cuts = len(cuts)
        cuts.sort()

        @lru_cache(None)
        def solve(i, j):

            if i > j: return 0

            mini = float('inf')
            for k in range(i, j+1):
                mini = min(solve(i, k-1) + solve(k+1, j) + cuts[j+1] - cuts[i-1], mini)

            return mini
        
        
        return solve(1, total_cuts - 2)
        