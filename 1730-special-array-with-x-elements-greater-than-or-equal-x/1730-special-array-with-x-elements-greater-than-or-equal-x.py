from typing import List


class Solution:
    def specialArray(self, nums: List[int]) -> int:
        n = len(nums)
        count = [0] * (1002)

        for num in nums:
            count[num] += 1

        # saving the count of numbers greater than or equal to i
        for i in range(1000, -1, -1):
            count[i] += count[i + 1]

        for i in range(1000, -1, -1):
            if i == count[i]:
                return i

        return -1
