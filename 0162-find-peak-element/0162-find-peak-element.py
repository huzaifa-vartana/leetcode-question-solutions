from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, n - 1
        
        while l <= r:
            m = (l + r) // 2

            # Check if middle is a peak
            left = nums[m - 1] if m > 0 else float('-inf')
            right = nums[m + 1] if m < n - 1 else float('-inf')
            
            if nums[m] > left and nums[m] > right:
                return m

            # Move to the side with the higher neighbor
            if nums[m] < right:
                l = m + 1
            else:
                r = m - 1

        return -1  # This line is never reached if there's always at least one peak
