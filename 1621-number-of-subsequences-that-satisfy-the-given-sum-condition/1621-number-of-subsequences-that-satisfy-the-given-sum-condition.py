import bisect
from typing import List


class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        ans = 0
        N = len(nums)

        nums.sort()
        for i, minimum_num in enumerate(nums):
            if minimum_num >= target: continue

            maximum_num = target - minimum_num
            # Find the first index where nums[j] > maximum_num
            j = bisect.bisect_right(nums, maximum_num, i)
            
            if j == i: continue
            ans += 2 ** (j - i - 1)


        return ans % (10**9 + 7)