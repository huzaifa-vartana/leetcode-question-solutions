class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        n = len(prices)


        cache = {}


        def solve(idx,  lastBought):

            if idx >= n: return 0
            state = (idx, lastBought)
            if state in cache: return cache[state]

            if not lastBought:
                cache[state] = max(-prices[idx] + solve(idx+1, True),
                                   solve(idx+1, False))
                return cache[state]
            else:
                cache[state] = max(prices[idx] + solve(idx+1, False),
                                   solve(idx+1, lastBought))
                return cache[state]

            
        return solve(0, False)