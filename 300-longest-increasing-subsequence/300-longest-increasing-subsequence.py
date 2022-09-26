class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        n = len(nums)
        cache = [1] * (n+1)
        
        lis = 0
        for idx in range(n):
            for prevIdx in range(idx):
                
                if nums[idx] > nums[prevIdx]: cache[idx] = max(cache[idx], 1 + cache[prevIdx])
                
            lis = max(lis, cache[idx])
                
        return lis