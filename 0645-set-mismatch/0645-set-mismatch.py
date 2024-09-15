from typing import List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        total_sum = sum(range(1, n+1))

        # missing number
        missing_number = total_sum - sum(set(nums))

        # duplicate number
        duplicate_number = sum(nums) - sum(set(nums))

        return [duplicate_number, missing_number]

