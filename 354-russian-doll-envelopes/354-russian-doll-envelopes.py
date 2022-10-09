class Solution:
    def maxEnvelopes(self, nums: List[List[int]]) -> int:
        
        n = len(nums)
        nums.sort(key = lambda x: [x[0], -x[1]])
        print(nums)
        
        def bs(key, arr):
            l, h = 0, len(arr) - 1
            while l <= h:
                mid = (l+h) // 2
                if arr[mid] == key: return mid
                elif arr[mid] > key: h = mid - 1
                else: l = mid + 1
            return l
            
            
        res = [nums[0][1]]
        for idx in range(1, n):
            if nums[idx][1] > res[-1]: res.append(nums[idx][1])
            else: res[bs(nums[idx][1], res)] = nums[idx][1]
            
        return len(res)