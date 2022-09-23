class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        n = len(prices)


        cache = [[-1 for _ in range(2)] for _ in range(n+1)]


        def solve(idx,  lastBought):

            if idx >= n: return 0
            if cache[idx][lastBought] != -1: return cache[idx][lastBought]

            if not lastBought:
                cache[idx][lastBought] = max(-prices[idx] + solve(idx+1, True),
                                   solve(idx+1, False))
                return cache[idx][lastBought]
            else:
                cache[idx][lastBought] = max(prices[idx] + solve(idx+1, False),
                                   solve(idx+1, lastBought))
                return cache[idx][lastBought]

            
        return solve(0, False)