class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        max_p = 0
        last_b = None
        for price in prices:
            if last_b is None or price < last_b:
                last_b = price
            elif price > last_b:
                max_p += price - last_b
                last_b = price

        return max_p
        