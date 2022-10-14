class Solution:
    def climbStairs(self, n: int) -> int:
        
        
        cache = [0] * (n+1)
        cache[n] = 1
        for idx in range(n-1, -1, -1):
            a = 0
            if idx+2 in range(n+1): a = cache[idx+2]
            cache[idx] = cache[idx+1] + a
        
        
        return cache[0]