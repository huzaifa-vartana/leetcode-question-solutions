from typing import List


class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:

        max_pair = []
        min_pair = []

        for num in nums:
            if len(max_pair) < 2:
                max_pair.append(num)
                min_pair.append(num)
                max_pair.sort()
                min_pair.sort()
            else:
                if num > max_pair[0]:
                    max_pair[0] = num
                    max_pair.sort()
                if num < min_pair[1]:
                    min_pair[1] = num
                    min_pair.sort()

        return (max_pair[1] * max_pair[0]) - (min_pair[0] * min_pair[1])