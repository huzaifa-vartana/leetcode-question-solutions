class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        
        n = len(prices)
        prev = [0 for _ in range(2)]
        last = [0 for _ in range(2)]
        for idx in range(n-1, -1, -1):
            curr = [0 for _ in range(2)]
            for buy in [True, False]:
                
                if buy:
                    curr[buy] = max(-prices[idx] + prev[False], prev[True])

                else:
                    # if idx+2 <= n: 
                    #     tmp = prices[idx] + prev[True]
                    # else:
                    #     tmp = prices[idx] + 0
                    tmp = prices[idx] + last[True]
                    curr[buy] = max(tmp, prev[buy])
                    
            last = prev.copy()
            prev = curr.copy()

            
        return prev[True]