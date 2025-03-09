class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:

        increasing = True
        decreasing = True
        for idx in range(1, len(nums)):
            increasing = increasing and nums[idx-1] <= nums[idx]
            decreasing = decreasing and nums[idx-1] >= nums[idx]

        return increasing or decreasing