class Solution:
    def lengthOfLIS(self, nums_: List[int]) -> int:
        n = len(nums_)

        def bs(nums, key):
            low, high = 0, len(nums) - 1
            while low <= high:
                mid = (low+high) // 2
                if nums[mid] == key:
                    return mid
                if nums[mid] > key:
                    high = mid - 1
                else:
                    low = mid + 1

            return low
        
        
        res = [nums_[0]]
        for idx in range(1, n):
            if nums_[idx] > res[-1]:
                res.append(nums_[idx])
            else:
                res[bs(res, nums_[idx])] = nums_[idx]
                
        return len(res)