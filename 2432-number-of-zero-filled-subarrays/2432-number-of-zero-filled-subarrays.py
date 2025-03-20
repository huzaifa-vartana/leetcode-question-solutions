from typing import List


class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        N = len(nums)
        left, right = 0, 0

        count = 0
        while right <= N:
            if right < N and nums[right] == 0:
                while right < N and nums[right] == 0:
                    right += 1
                    count += right - left
            else:
                right += 1
                left = right


        return count