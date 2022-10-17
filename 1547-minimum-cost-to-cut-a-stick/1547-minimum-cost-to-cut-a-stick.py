class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        
        # cache = [[-1 for _ in range(n+1)] for _ in range(n+1)]
        cache = {}
        def solve(i, j):
            
            state = (i, j)
            if state in cache: return cache[state]
            
            mini = float('inf')
            for cut in cuts:
                if i < cut < j:

                    mini = min(
                        mini,
                        j - i + solve(i, cut) + solve(cut, j)
                    )
            cache[state] = 0 if mini == float('inf') else mini
            return cache[state]

        
        
        return solve(0, n)