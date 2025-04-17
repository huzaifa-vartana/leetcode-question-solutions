class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        window_sum, mini, N = 0, float('inf'), len(nums)

        l = 0
        for r in range(N):
            window_sum += nums[r]

            while window_sum >= target:
                mini = min(mini, r - l + 1)
                window_sum -= nums[l]
                l += 1


        return 0 if mini == float('inf') else mini
        