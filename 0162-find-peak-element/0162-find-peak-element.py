class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        n = len(nums)
        low, high = 0, n - 1

        if n == 1: return 0
                
        if nums[0] > nums[1]: return 0
        if nums[n-1] > nums[n-2]: return n-1


        while low <= high:
            mid = (low + high) // 2

            # check if findPeakElement
            if (mid + 1) in range(0, n) and (mid - 1) in range(0, n) and nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]:
                return mid

            # divide search space
            if (mid + 1) in range(0, n) and nums[mid] <= nums[mid+1]:
                low = mid + 1
            else:
                high = mid - 1










        return -1