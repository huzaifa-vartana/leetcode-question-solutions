class Solution:
    def maxEnvelopes(self, nums: List[List[int]]) -> int:
        
        nums.sort(key = lambda d: [d[0], -d[1]])
        n = len(nums)
        
        def upper_bound(target, arr):
            l, h = 0, len(arr) - 1
            while l < h:
                mid = (l+h) // 2
                if target <= arr[mid]:
                    h = mid # we dont do mid - 1 since we also want next greater element
                else:
                    l = mid + 1
            return l
                    
        
        rs = [nums[0][1]]
        for idx in range(1, n):
            if nums[idx][1] > rs[-1]: rs.append(nums[idx][1])
            else:
                rs[upper_bound(nums[idx][1], rs)] = nums[idx][1]
            
            
        return len(rs)
        

        
        
        