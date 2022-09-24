class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        n = len(prices)


        # cache = [[float('-inf') for _ in range(2)] for _ in range(n+1)]
        # cache[n][True] = 0
        # cache[n][False] = 0
        curr, prev = [float('-inf')] * (2), [float('-inf')] * (2)
        prev[False] = prev[True] = 0
        for idx in range(n-1, -1, -1):
            for lastBought in [True, False]:

                if not lastBought:
                    curr[lastBought] = max(-prices[idx] + prev[True], prev[False])
                else:
                    curr[lastBought] = max(prices[idx] + prev[False], prev[lastBought])
            
            prev = curr.copy()
            
        return prev[False]