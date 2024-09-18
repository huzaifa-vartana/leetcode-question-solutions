from typing import List


class Solution:
    def specialArray(self, nums: List[int]) -> int:
        n = len(nums)
        count = [0] * (n + 1)

        for num in nums:
            count[min(num, n)] += 1

        for i in range(n, 0, -1):
            count[i - 1] += count[i]
            if count[i] == i:
                return i

        return -1
