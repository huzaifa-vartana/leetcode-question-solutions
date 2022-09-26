class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        
        
        n = len(prices)
        prev = [0 for _ in range(2)]
        for idx in range(n-1, -1, -1):
            curr = [0 for _ in range(2)]
            for buy in [True, False]:
                if buy:
                    curr[buy] = max(-prices[idx] + prev[False], prev[True])
                else:
                    curr[buy] = max(prices[idx] - fee + prev[True], prev[buy])
            prev = curr
            
        return prev[True]
        