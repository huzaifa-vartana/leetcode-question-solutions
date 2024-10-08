from typing import List


class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        N = len(nums)
        nums.sort(reverse=True)
        left = 0

        res = float('inf')

        for right in range(k-1, N):
            res = min(res, nums[left] - nums[right])
            left += 1

        return res
