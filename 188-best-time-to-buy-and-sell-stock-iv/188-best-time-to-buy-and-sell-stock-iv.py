class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        
        
        
        
        n = len(prices)
        totalTrans = 2 * k
        prev = [0 for _ in range(totalTrans + 1)]
        for idx in range(n-1, -1, -1):
            curr = [0 for _ in range(totalTrans + 1)]
            for trans in range(totalTrans - 1, -1, -1):

                buy = trans % 2 == 0
            
                if buy:
                    curr[trans] = max(-prices[idx] + prev[trans+1], prev[trans])
                else:
                    curr[trans] = max(prices[idx] + prev[trans+1], prev[trans])
            prev = curr
                
        
        return prev[0]
        