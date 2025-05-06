class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        n = len(nums)
        ans = 0
        
        for i in range(n):
            # Find the range of indices where nums[i] + nums[j] is within [lower, upper]
            left = bisect.bisect_left(nums, lower - nums[i], i + 1)
            right = bisect.bisect_right(nums, upper - nums[i], i + 1)
            ans += right - left
        
        return ans