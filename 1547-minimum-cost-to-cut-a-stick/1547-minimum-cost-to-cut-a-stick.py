class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        
        cuts.append(0)
        cuts.append(n)
        cuts.sort()
        n = len(cuts)
        cache = [[-1 for _ in range(n+1)] for _ in range(n+1)]
        
        @lru_cache(None)
        def solve(i, j):

            if i > j: return 0
            # if cache[i][j] != -1: return cache[i][j]
            
            mini = float('inf')
            for k in range(i, j+1):

                mini = min(
                    mini,
                    cuts[j+1] - cuts[i-1] + solve(i, k-1) + solve(k+1, j)
                )
            # cache[i][j] = mini
            # return cache[i][j]
            return mini

        
        return solve(1, n-2)