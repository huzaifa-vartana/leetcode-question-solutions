class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        
        nums = [1] + nums + [1]
        n = len(nums)
        cache = [[-1 for i in range(n+1)]for j in range(n+1)]
        
        def solve(i, j):
            if i > j: return 0
            if cache[i][j] !=-1: return cache[i][j]
            
            
            maxi = float('-inf')
            for k in range(i, j+1):
                
                maxi = max(
                    maxi, 
                    solve(i, k-1) + solve(k+1, j) + nums[i-1] * nums[k] * nums[j+1]
                )
                
            cache[i][j] = maxi
            return cache[i][j] 
        
        
        return solve(1, n-2)