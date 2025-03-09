from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        N = len(nums)
        for idx in range(N):
            num = abs(nums[idx])
            val = num - 1
            if nums[val] >= 0:
                nums[val] = -1 * nums[val]

        res = []
        for idx in range(N):
            if nums[idx] > 0:
                res.append(idx+1)
        return res