from typing import List


class Solution:
    def specialArray(self, nums: List[int]) -> int:

        nums.sort()
        max_num = nums[-1]
        n = len(nums)

        def binary_search(nums, target):
            left, right = 0, len(nums) - 1
            while left < right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid
            return len(nums) - left

        cache = {}
        for i in range(max_num + 1):

            if i in cache:
                if cache[i] == i:
                    return i
                continue

            # find out how many elements are greater than or equal to i using binary search
            count = binary_search(nums, i)
            cache[i] = count
            if count == i:
                return i

        return -1
