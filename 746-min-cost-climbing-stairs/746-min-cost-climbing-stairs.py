class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        
        
        n = len(cost)
        cache = [0] * (n+1)
        for idx in range(n-1, -1, -1):
            
            b = float('inf')
            if idx+2 in range(n+1): b = cost[idx] + cache[idx+2]
            cache[idx] = min(cost[idx] + cache[idx+1], b)
        
        return min(cache[0], cache[1])