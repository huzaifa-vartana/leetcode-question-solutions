from typing import List


class Solution:
    def specialArray(self, nums: List[int]) -> int:

        # nums.sort()
        max_num = max(nums)

        for i in range(max_num + 1):
            if i == sum(1 for num in nums if num >= i):
                return i

        return -1