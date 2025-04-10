class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return 0


        max_profit, min_price_so_far = 0, float('inf')
        for price in prices:
            min_price_so_far = min(min_price_so_far, price)
            max_profit = max(max_profit, price - min_price_so_far)


        return max_profit
        