class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        n = len(prices)


        cache = [[float('-inf') for _ in range(2)] for _ in range(n+1)]
        cache[n][True] = 0
        cache[n][False] = 0
        for idx in range(n-1, -1, -1):
            for lastBought in [True, False]:

                if not lastBought:
                    cache[idx][lastBought] = max(-prices[idx] + cache[idx+1][True], cache[idx+1][False])
                else:
                    cache[idx][lastBought] = max(prices[idx] + cache[idx+1][False], cache[idx+1][lastBought])

            
        return cache[0][False]