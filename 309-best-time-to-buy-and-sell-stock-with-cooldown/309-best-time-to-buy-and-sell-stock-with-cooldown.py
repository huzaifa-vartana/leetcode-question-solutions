class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        
        n = len(prices)
        cache = [[-1 for _ in range(2)] for _ in range(n+1)]
        
        
        def solve(idx, buy):
            
            if idx >= n: return 0
            if cache[idx][buy] != -1: return cache[idx][buy]
            
            if buy:
                cache[idx][buy] = max(-prices[idx] + solve(idx+1, False), solve(idx+1, True))
                return cache[idx][buy]
            else:
                cache[idx][buy] = max(prices[idx] + solve(idx+2, True), solve(idx+1, buy))
                return cache[idx][buy]
            
            
            
        return solve(0, True)