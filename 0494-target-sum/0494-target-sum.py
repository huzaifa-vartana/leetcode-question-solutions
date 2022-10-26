class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        
        n = len(nums)
        t = target
        tot = sum(nums)
        d = (tot-t) // 2
        if (tot-t) < 0 or (tot-t) % 2 != 0: 
            return 0
        
        cache = [[-1 for _ in range(d+1)] for _ in range(n+1)]
        def solve(idx, t):
            if idx >= n: return 1 if t == d else 0
            if t > d: return 0
            if cache[idx][t] != -1: return cache[idx][t]
            
            cache[idx][t] = solve(idx+1, t + nums[idx]) + solve(idx+1, t)
            return cache[idx][t] 
        
        

        return solve(0, 0)
            
        
        
        