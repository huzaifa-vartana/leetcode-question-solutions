from typing import List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:

        n = len(nums)
        rep = None
        mis = None
        for idx in range(1, n+1):
            new_idx = abs(nums[idx-1])
            if nums[new_idx-1] > 0:
                nums[new_idx-1] = -nums[new_idx-1]
            else:
                rep = new_idx

        for idx in range(n):
            if nums[idx] > 0:
                mis = idx+1
                break

        return [rep, mis]