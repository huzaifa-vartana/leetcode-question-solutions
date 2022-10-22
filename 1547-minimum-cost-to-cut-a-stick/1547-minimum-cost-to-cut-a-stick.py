class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        
        cuts.append(0)
        cuts.append(n)
        cuts.sort()
        c = len(cuts)
        cache = [[0 for _ in range(c+1)] for _ in range(c+1)]
        for i in range(c, 0, -1):
            for j in range(i, c-1):
            
                mini = float('inf')
                for k in range(i, j+1):
                    mini = min(
                        mini,
                        cuts[j+1] - cuts[i-1] + cache[i][k-1] + cache[k+1][j]
                    )
                cache[i][j] = mini

            
            
        return cache[1][c-2]