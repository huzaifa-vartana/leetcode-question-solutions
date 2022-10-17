class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        
        cuts.append(0)
        cuts.append(n)
        cuts.sort()
        n = len(cuts)
        cache = [[0 for _ in range(n+1)] for _ in range(n+1)]
        
        for i in range(n, -1, -1):
            for j in range(i, n-1):
                
                mini = float('inf')
                for k in range(i, j+1):

                    mini = min(
                        mini,
                        cuts[j+1] - cuts[i-1] + cache[i][k-1] + cache[k+1][j]
                    )
                cache[i][j] = mini


        return cache[1][n-2]