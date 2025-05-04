import bisect


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        N = len(nums)
        # lower bound
        lower_bound = self.lower_bound(nums, target)

        # upper bound
        upper_bound = self.upper_bound(nums, target)

        # check if target is not in the list
        if lower_bound == N or nums[lower_bound] != target:
            return [-1, -1]

        return [lower_bound, upper_bound - 1]

    def lower_bound(self, nums, target):
        N = len(nums)
        ans = N

        low, high = 0, N - 1
        while low <= high:
            mid = low + (high-low) // 2

            if nums[mid] >= target:
                ans = mid
                high = mid - 1
            else: low = mid + 1
        return ans

    def upper_bound(self, nums, target):
        N = len(nums)
        ans = N

        low, high = 0, N - 1
        while low <= high:
            mid = low + (high-low) // 2

            if nums[mid] > target:
                ans = mid
                high = mid - 1
            else: low = mid + 1
        return ans