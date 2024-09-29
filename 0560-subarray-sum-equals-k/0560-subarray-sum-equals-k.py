from collections import defaultdict
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        N = len(nums)
        count = 0
        prefix = defaultdict(int)
        prefix[0] = 1
        cum_sum = 0

        for num in nums:
            cum_sum += num

            if (cum_sum - k) in prefix:
                count += prefix[(cum_sum - k)]

            prefix[cum_sum] += 1

        return count
