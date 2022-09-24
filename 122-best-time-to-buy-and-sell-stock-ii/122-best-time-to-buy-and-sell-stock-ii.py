class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        n = len(prices)
        
        prev = [float('-inf')] * (2)
        prev[False] = prev[True] = 0
        
        for idx in range(n-1, -1, -1):
            curr = [float('-inf')] * (2)
            for lastBought in [True, False]:

                if not lastBought:
                    curr[lastBought] = max(-prices[idx] + prev[True], prev[False])
                else:
                    curr[lastBought] = max(prices[idx] + prev[False], prev[lastBought])
            
            prev = curr.copy()
            
        return prev[False]