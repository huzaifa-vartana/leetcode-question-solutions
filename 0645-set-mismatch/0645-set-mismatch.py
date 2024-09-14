from typing import List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        for i in range(n - 1):
            if nums[i] == nums[i + 1]:
                duplicate = nums[i]
                break
        total = n * (n + 1) // 2
        missing = total - sum(set(nums))
        return [duplicate, missing]