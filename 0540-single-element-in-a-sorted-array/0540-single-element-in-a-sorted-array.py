from typing import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        left, right = 0, len(nums) - 1

        """
        len of array will be odd
        we have divide the array on the basis of the length of the left and right parts

        """

        while left <= right:
            mid = (left+right) // 2

            # check if mid is single element - left and right neighbors should not be the same or not exist

            if ((mid-1) not in range(n) or nums[mid-1] != nums[mid]) and ((mid+1) not in range(n) or nums[mid+1] != nums[mid]):
                return nums[mid]

            # eliminate the left and right arrays
            length_of_left_part = mid-1 if nums[mid] == nums[mid-1] else mid
            length_of_right_part = n - length_of_left_part
            if length_of_left_part % 2 != 0:
                # left part is odd
                right = mid - 1
            else:
                # left part is even
                left = mid + 1
        return -1