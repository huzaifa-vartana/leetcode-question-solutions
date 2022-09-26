class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        def bs(arr, t):
            left, right = 0, len(arr) - 1
            while left <= right:
                mid = (left+right) // 2
                if arr[mid] == t: 
                    return mid
                elif arr[mid] < t:
                    left = mid + 1
                else:
                    right = mid - 1
                    
            return left
        
        n = len(nums)
        lis = [nums[0]]
        for idx in range(1, n):
            if nums[idx] > lis[-1]:
                lis.append(nums[idx])
            else:
                tmp = bs(lis, nums[idx])
                lis[tmp] = nums[idx] 
        
        return len(lis)
            
        
        
        
        
        
        
        
        
        
#         n = len(nums)
#         cache = [1] * (n+1)
        
#         lis = 0
#         for idx in range(n):
#             for prevIdx in range(idx):
                
#                 if nums[idx] > nums[prevIdx]: cache[idx] = max(cache[idx], 1 + cache[prevIdx])
                
#             lis = max(lis, cache[idx])
                
#         return lis