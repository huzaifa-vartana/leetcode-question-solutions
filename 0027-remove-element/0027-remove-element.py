from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        start = 0
        N = len(nums)
        end = N - 1
        swaps = 0

        while start < end:
            if nums[start] == val and nums[end] == val:
                end -= 1

            elif nums[start] != val and nums[end] == val:
                start += 1
                end -= 1
                swaps += 1

            elif nums[start] == val and nums[end] != val:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
                swaps += 1

            elif nums[start] != val and nums[end] != val:
                start += 1
                swaps += 1

        if start == end and nums[start] != val:
            swaps += 1

        return swaps
