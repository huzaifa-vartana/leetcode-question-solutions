from typing import List


class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        N = len(nums)
        res = []

        prefix = [0] * (N+1)
        suffix = [0] * (N+1)
        for i in range(1, N+1):
            prefix[i] = prefix[i-1] + nums[i-1]
        for i in range(N-1, -1, -1):
            suffix[i] = suffix[i+1] + nums[i]
        
        for i in range(N):
            left = i * nums[i] - prefix[i]
            right = suffix[i+1] - (N-i-1) * nums[i]
            res.append(left + right)

        return res