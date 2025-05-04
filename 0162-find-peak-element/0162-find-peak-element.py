from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, n - 1
        while l < r:
            m = (l+r) // 2
            if (m == 0 and nums[m] > nums[m+1]) or (m == n - 1 and nums[m] > nums[m-1]):
                return m
            if m+1 in range(n) and nums[m] > nums[m+1] and m-1 in range(n) and nums[m] > nums[m-1]:
                return m

            if m+1 in range(n) and nums[m] < nums[m+1]:
                l = m + 1
            else:
                r = m - 1

        return l
