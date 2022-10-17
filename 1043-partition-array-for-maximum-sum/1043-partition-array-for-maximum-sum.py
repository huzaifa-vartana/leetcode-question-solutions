class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], max_length: int) -> int:
        
        
        n = len(arr)
        
        @lru_cache(None)
        def solve(idx):
            
            if idx >= n: return 0
            
            maxi = float('-inf')
            for k in range(idx, min(idx+max_length, n)):
                tmp = max(arr[idx:k+1]) * (k - idx + 1)
                maxi = max(
                    maxi,
                    tmp + solve(k+1)
                )
            
            
            return maxi
            
            
        return solve(0)