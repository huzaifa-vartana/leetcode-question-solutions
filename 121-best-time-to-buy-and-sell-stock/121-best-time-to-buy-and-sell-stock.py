class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        n = len(prices)
        mini = prices[0]
        profit = 0
        for price in prices:
            profit = max(profit, price - mini)
            mini = min(mini, price)
            
        return profit