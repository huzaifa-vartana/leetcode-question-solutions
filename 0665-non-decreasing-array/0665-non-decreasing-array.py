from typing import List


class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        N = len(nums)

        swaps = 0
        for i in range(N-1):
            if nums[i] <= nums[i + 1]:
                continue

            if i == 0 or nums[i-1] <= nums[i+1]:
                nums[i] = nums[i+1]
            else:
                nums[i+1] = nums[i]

            swaps += 1

        return swaps == 0 or swaps == 1
