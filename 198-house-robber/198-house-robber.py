class Solution:
    def rob(self, nums: List[int]) -> int:
        
        
        n = len(nums)
        cache = [0] * (n+1)
        for idx in range(n-1, -1, -1):
            
            rob = nums[idx]
            if idx+2 in range(n+1): rob = nums[idx] + cache[idx+2]
            nrob = cache[idx+1]
            cache[idx] = max(rob, nrob)
        
        return cache[0]