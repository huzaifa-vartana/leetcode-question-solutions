class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        
        
        n = len(nums)
        cache = [1] * (n+1)
        count = [1] * (n+1)
        maxi, countMaxi = 1, 1
        for idx in range(1, n):
            for prevIdx in range(idx):
                if nums[idx] > nums[prevIdx]:
                    if 1 + cache[prevIdx] > cache[idx]:
                        cache[idx], count[idx] = 1 + cache[prevIdx], count[prevIdx] 
                    elif cache[idx] == 1 + cache[prevIdx]:
                        count[idx] += count[prevIdx] 
            
            
            if cache[idx] > maxi:
                maxi = cache[idx]
                countMaxi = count[idx]
            elif cache[idx] == maxi:
                countMaxi += count[idx]
          

        return countMaxi