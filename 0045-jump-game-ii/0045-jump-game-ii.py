class Solution:
    def jump(self, nums: List[int]) -> int:
        
        
        
        n = len(nums)
        cache = [-1] * (n+1)
        
        @lru_cache(None)
        def solve(idx):
            if idx == n - 1: return 0
            if idx >= n: return float('inf')
            
            count = float('inf')
            for jump in range(1, nums[idx]+1):
                count = min(count, 1 + solve(idx+jump))
            
            return count
        
        
        
        return solve(0)
        