class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        

        nums = [1] + nums + [1]
        n = len(nums)
        cache = [[0 for _ in range(n+1)] for _ in range(n+1)]
        

        for i in range(n-2, 0, -1):
            for j in range(i, n-1):


                maxi = float('-inf')
                for k in range(i, j+1):

                    maxi = max(
                        maxi,
                        cache[i][k-1] + cache[k+1][j] + nums[i-1] * nums[k] * nums[j+1]
                    )

                cache[i][j] = max(maxi, cache[i][j])
        
        return cache[1][n-2]