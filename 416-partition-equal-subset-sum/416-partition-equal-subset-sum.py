class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        
        n = len(nums)
        tot = sum(nums)
        if tot % 2 != 0: return False
        partSum = tot // 2
        cache = {}
        def solve(idx, s):
            
            if s == partSum: return True
            if s > partSum: return False
            if idx >= n: return True if s == partSum else False
            state = (idx, s)
            if state in cache: return cache[state]
            
            cache[state] = solve(idx+1, s+nums[idx]) or solve(idx+1, s)
            return cache[state] 
            
        
        return solve(0, 0)