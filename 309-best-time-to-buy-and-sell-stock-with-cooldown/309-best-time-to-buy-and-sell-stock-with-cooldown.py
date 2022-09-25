class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        
        n = len(prices)
        cache = [[0 for _ in range(2)] for _ in range(n+1)]
        for idx in range(n-1, -1, -1):
            for buy in [True, False]:
                
                if buy:
                    cache[idx][buy] = max(-prices[idx] + cache[idx+1][False], cache[idx+1][True])

                else:
                    if idx+2 <= n: 
                        tmp = prices[idx] + cache[idx+2][True]
                    else:
                        tmp = prices[idx] + 0
                    cache[idx][buy] = max(tmp, cache[idx+1][buy])

            
            
            
        return cache[0][True]