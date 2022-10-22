class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        
        
        
        
        n = len(nums)
        count = [1] * (n)
        lis = [1] * (n)

        maxLisLength = 1
        for i in range(n):
            for p in range(i):
                if nums[i] > nums[p]:
                    if lis[i] < 1 + lis[p]:
                        lis[i] = 1 + lis[p]
                        count[i] = count[p]
                    elif lis[i] == 1 + lis[p]:
                        count[i] += count[p]
                        
            maxLisLength = max(maxLisLength, lis[i])
        

        c = 0
        for i, maxL in enumerate(lis):
            if maxL == maxLisLength:
                c += count[i]
            
            
            
        return c